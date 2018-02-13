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
