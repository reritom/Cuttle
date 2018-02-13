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
