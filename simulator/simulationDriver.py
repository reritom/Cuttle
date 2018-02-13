class SimulationDriver():
    '''
        Used to simulate the DriveManger with time and command variations.
        To be inherited (maybe) by the other classes
    '''
    def __init__(self):
        pass

    def addEvent(self):
    '''
        Add an event like injecting a message into the DriveManager
    '''
    pass

    def runSimulation(self):
    '''
        This method loops and injects events at given times if present
    '''
    pass
