class DriverControl(object):
    '''
        This class is used for creating an 8 bit binary message to shift to the driver
        representing commands
    '''
    def __init__(self):
        self.status = False
        self.control = [0 for i in range(8)]

        '''
        The control register has 8 bits, with the following specs:

        0 - Active/Inactive
        1 - Speed MSB
        2 - Speed
        3 - Speed
        4 - Speed LSB
        5 - Unspecified
        6 - Unspecified
        7 - Reboot
        '''

    def setActive(self):
        '''
            This sets whether the driver should be active or not
        '''
        self.control[0] = 1

    def setReboot(self):
        '''
            This method sets the reboot pin
        '''
        self.control[7] = 1

    def setSpeed(self, speedString):
        '''
            The speed takes up 4 bits representing a value between 0-(2^4-1)
        '''
        speedBits = [1, 2, 3, 4]

        for i in range(4):
            self.control[speedBits[i]] = int(speedString[i])

    def getBinary(self):
        '''
            This method returns the binary reprentation of the command
        '''
        return self.control
