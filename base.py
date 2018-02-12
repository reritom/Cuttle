class DriveManager():
    '''
        This class parses a command which is split and sent to both the portside and starboard TrackDrivers
    '''
    def __init__(self):
        self.incomingSerial = None
        self.serialMessage = None
        self.trackDrivers = {'Portside': TrackDriver(),
                             'Starboard': TrackDriver()}
        pass



    def serialRead(self):
        '''
            Parse the incoming serial command. Split it into a command for each drive, then shift out the command to
            each command_register
        '''
        if self.incomingSerial is not None:
            self.serialMessage = self.incomingSerial
            self.incomingSerial = None
        pass

    def parseSerial(self):
        '''
            Parse the serial input
        '''
        pass

    def processRound(self):
        '''
            This method processes the current round in the loop
        '''
        # If serial, read it, else finish round

        # parse the serial
        pass

class TrackDriver():
    '''
        This class reads from the command register and shifts out bits to control the track relays
    '''
    def __init__(self):
        self.command_register = [0 for i in range(8)]
        self.status_register = [0 for i in range(8)]
        pass

    def readCommand(self):
        '''
            Check if the command has updated. If so, implement new command, else continue
        '''
        # Check the first bit
        pass

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
