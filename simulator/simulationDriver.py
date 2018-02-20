from trackManager import TrackManager

class SimulationDriver():
    '''
        Used to simulate the DriveManger with time and command variations.
        To be inherited (maybe) by the other classes
    '''
    def __init__(self, rounds):
        self.createObject()
        self.rounds = rounds
        self.events = {}

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
        self.events[at] = action

    def runSimulation(self):
        '''
            This method loops and injects events at given times if present
        '''
        for this_round in range(self.rounds):
            if self.events.get(this_round, False):
                self.components['Manager'].incomingSerial = self.events[this_round]

            for component in self.components:
                self.components[component].runRound()


if __name__ == '__main__':
    sim = SimulationDriver(rounds=20)
    sim.addEvent(10, "GO")
    sim.runSimulation()
