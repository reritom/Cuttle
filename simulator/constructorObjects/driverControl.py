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
        1 - Reboot
        2 - Direction (1f, 0r)
        3 - Override
        4 - Speed MSB
        5 - Speed
        6 - Speed
        7 - Speed LSB
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
        self.control[1] = 1

    def setDirection(self):
        '''
            This method sets the direction bit, 1 for forward, 0 for reverse
        '''
        self.control[2] = 1

    def setOverride(self):
        '''
            This method sets the override bit.
            This is used for interpretting the speed bits as multipliers instead of set speeds
        '''
        self.control[3] = 1

    def setSpeed(self, speedString):
        '''
            The speed takes up 4 bits representing a value between 0-(2^4-1)
        '''
        speedBits = [4, 5, 6, 7]

        for i in range(4):
            self.control[speedBits[i]] = int(speedString[i])

    def getBinary(self):
        '''
            This method returns the binary reprentation of the command
        '''
        return self.control
