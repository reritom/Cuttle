class DriverControl(object):
    '''
        This class is used for creating an 8 bit binary message to shift to the driver
        representing commands
    '''
    def __init__(self):
        self.status = False
        self.speed = 0 # Value between 0 and (2^4)-1

    def setStatus(self, boolean):
        '''
            This sets whether the driver should be active or not
        '''
        pass

    def getBinary(self):
        '''
            This method returns the binary reprentation of the command
        '''
        return 'BinaryList'
