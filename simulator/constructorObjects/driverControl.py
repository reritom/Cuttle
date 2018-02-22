class DriverControl(object):
    '''
        This class is used for creating an 8 bit binary message to shift to the driver
        representing commands
    '''
    def __init__(self):
        self.status = False
        self.control_bits = {'Active': 0,
                            'Reboot': 0,
                            'Direction': 0,
                            'Override': 0,
                            'SpeedMSB': 0,
                            'SpeedMSM': 0,
                            'SpeedLSM': 0,
                            'SpeedLSB': 0}

        self.bit_order = ['Active',
                          'Reboot',
                          'Direction',
                          'Override',
                          'SpeedMSB',
                          'SpeedMSM',
                          'SpeedLSM',
                          'SpeedLSB']

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
        self.control_bits['Active'] = 1

    def getActive(self):
        return self.control_bits['Active']

    def setReboot(self):
        '''
            This method sets the reboot pin
        '''
        self.control_bits['Reboot'] = 1

    def getReboot(self):
        return self.control_bits['Reboot']

    def setDirection(self):
        '''
            This method sets the direction bit, 1 for forward, 0 for reverse
        '''
        self.control_bits['Direction'] = 1

    def getDirection(self):
        return self.control_bits['Direction']

    def setOverride(self):
        '''
            This method sets the override bit.
            This is used for interpretting the speed bits as multipliers instead of set speeds
        '''
        self.control_bits['Override'] = 1

    def getOverride(self):
        return self.control_bits['Override']

    def setSpeed(self, speed_string):
        '''
            The speed takes up 4 bits representing a value between 0-(2^4-1)
        '''
        self.control_bits['SpeedMSB'] = speed_string[0]
        self.control_bits['SpeedMSM'] = speed_string[1]
        self.control_bits['SpeedLSM'] = speed_string[2]
        self.control_bits['SpeedLSB'] = speed_string[3]

    def getBinary(self):
        '''
            This method returns the binary reprentation of the command
        '''
        return [self.control_bits[i] for i in self.bit_order]

    def setBinary(self, binary_string):
        '''
            This method receives a string 'xxxxxxxx' and parses it into the register model
        '''
        for count, elem in enumerate(self.bit_order):
            self.control_bits[elem] = binary_string[count]
