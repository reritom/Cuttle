from trackManager import TrackManager
import time, sys
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

        self.components = {'Manager': manager,
                           'PortDriver': manager.trackDrivers['Portside'],
                           'StarDriver': manager.trackDrivers['Starboard']}

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
                print("Time to sample")
                this_log = dict()
                this_log['time'] = current_time - start_time

                self.components['Manager'].runRound(delta=delta)
                StarboardSky, StarboardDown = self.components['StarDriver'].runRound(delta=delta)
                PortsideSky, PortsideDown = self.components['PortDriver'].runRound(delta=delta)

                this_log['StarboardSky'] = StarboardSky
                this_log['StarboardDown'] = StarboardDown
                this_log['PortsideSky'] = PortsideSky
                this_log['PortsideDown'] = PortsideDown

                #print(this_log)
                self.logs.append(this_log)
                print(self.logs[-1])
                time_since_last_sample = 0
            else:
                # Run round without collecting logs
                for component in self.components:
                    self.components[component].runRound(delta=delta)
                time_since_last_sample += current_time - previous_time


            previous_time = current_time
            current_time = time.time()

        #print(self.logs)

        mydict_as_string = cPickle.dumps(self.logs)
        print(sys.getsizeof(mydict_as_string))


if __name__ == '__main__':
    sim = SimulationDriver(duration=20, sampling=1) #0.04
    sim.addEvent(5, "ST050:PR100") #Frequency (will default to 10 bit half wave size)
    sim.addEvent(10, "SW050") #50% pwm
    sim.addEvent(15, "SR050") #Change direction and reduce speed

    sim.runSimulation()
