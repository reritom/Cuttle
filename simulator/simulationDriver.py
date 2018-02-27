from trackManager import TrackManager
import time

class SimulationDriver():
    '''
        Used to simulate the DriveManger with time and command variations.
        To be inherited (maybe) by the other classes
    '''
    def __init__(self, duration):
        self.createObject()
        self.duration = duration
        self.events = []

    def createObject(self):
        '''
            This method creates a track, and lists all the objects that need running
        '''
        manager = TrackManager()

        self.components = {'Manager': manager,
                           #'PortDriver': manager.trackDrivers['Portside'],
                           'StarDriver': manager.trackDrivers['Starboard']}

    def addEvent(self, at, action):
        '''
            Add an event like injecting a message into the DriveManager
        '''
        self.events.append([at, action])

    def runSimulation(self):
        '''
            This method loops and injects events at given times if present
        '''
        start_time = time.time()
        current_time = start_time
        previous_time = start_time

        while current_time - start_time < self.duration:
            if self.events and self.events[0][0] < current_time - start_time:
                self.components['Manager'].incomingSerial = self.events[0][1]
                self.events.pop(0)

            for component in self.components:
                self.components[component].runRound(delta=current_time - previous_time)

            previous_time = current_time
            current_time = time.time()



if __name__ == '__main__':
    sim = SimulationDriver(duration=10)
    sim.addEvent(5, "ST050") #Frequency (will default to 10 bit half wave size)
    sim.addEvent(10, "SW050") #50% pwm
    sim.addEvent(15, "SR050") #Change direction and reduce speed

    sim.runSimulation()
