from track.track_manager import TrackManager
from physical_models.fin.fin_manager import FinManager
import time, sys
from config import Config
import _pickle as cPickle

class SimulationDriver():
    '''
        Used to simulate the DriveManger with time and command variations.
        To be inherited (maybe) by the other classes
    '''
    def __init__(self, duration, sampling):
        self.createObject()
        self.duration = duration
        self.sampling = sampling # Sample rate in seconds
        self.logs = []
        self.events = []

    def createObject(self):
        '''
            This method creates a track, and lists all the objects that need running
        '''
        manager = TrackManager()
        fins = FinManager(Config.DaisyChainSize)

        self.components = {'Manager': manager,
                           'PortDriver': manager.trackDrivers['Portside'],
                           'StarDriver': manager.trackDrivers['Starboard'],
                           'FinManager': fins}

    def addEvent(self, at, action):
        '''
            Add an event like injecting a message into the DriveManager
        '''
        self.events.append([at, action])

    def getLogs(self):
        '''
            This method retrieves the logs from the simulation
        '''
        return self.logs

    def runSimulation(self):
        '''
            This method loops and injects events at given times if present
        '''
        start_time = time.time()
        current_time = start_time
        previous_time = start_time

        time_since_last_sample = 0

        while current_time - start_time < self.duration:
            # Inject a predefined event into the manager serial buffer
            if self.events and self.events[0][0] < current_time - start_time:
                self.components['Manager'].incomingSerial = self.events[0][1]
                self.events.pop(0)

            delta = current_time - previous_time

            # If it is time to sample
            if time_since_last_sample > self.sampling:
                this_log = dict()
                this_log['time'] = current_time - start_time

                self.components['Manager'].runRound(delta=delta)
                StarboardTrit = self.components['StarDriver'].runRound(delta=delta)
                PortsideTrit = self.components['PortDriver'].runRound(delta=delta)

                starboard_fin_positions, portside_fin_positions = self.components['FinManager'].runRound(StarboardTrit, PortsideTrit, delta)

                this_log['StarboardTrit'] = StarboardTrit
                this_log['PortsideTrit'] = PortsideTrit
                this_log['StarboardFins'] = starboard_fin_positions
                this_log['PortsideFins'] = portside_fin_positions


                self.logs.append(this_log)

                if not Config.Debug:
                    percent = ((current_time - start_time)/self.duration)*100
                    self.progress(percent)

                time_since_last_sample = 0
            else:
                # Run round without collecting logs
                self.components['Manager'].runRound(delta=delta)
                StarboardTrit = self.components['StarDriver'].runRound(delta=delta)
                PortsideTrit = self.components['PortDriver'].runRound(delta=delta)
                self.components['FinManager'].runRound(StarboardTrit, PortsideTrit, delta)

                time_since_last_sample += current_time - previous_time

            previous_time = current_time
            current_time = time.time()

        print("Run of simulation complete")

    def progress(self, percent):
        '''
            This method prints a refreshing progress percentage. Any print statement
            which happens between successive calls to this, need to print something longer than
            the progress string
        '''
        percent = str(int(percent))

        padded_val = percent
        while len(padded_val) < 3:
            padded_val = " " + padded_val

        full_string = padded_val + "% percent complete".format("%")
        print(full_string, end="\r")



if __name__ == '__main__':
    sim = SimulationDriver(duration=20, sampling=1) #0.04
    sim.addEvent(5, "ST050:PR100") #Frequency (will default to 10 bit half wave size)
    sim.addEvent(10, "SW050") #50% pwm
    sim.addEvent(15, "SR050") #Change direction and reduce speed

    sim.runSimulation()
