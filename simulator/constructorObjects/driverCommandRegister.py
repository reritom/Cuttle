class DriverCommandRegister(object):
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
                            'FreeBit1': 0,
                            'FreeBit2': 0,
                            'FreeBit3': 0,
                            'FreeBit4': 0}

        self.bit_order = ['Active',
                          'Reboot',
                          'Direction',
                          'Override',
                          'FreeBit1',
                          'FreeBit2',
                          'FreeBit3',
                          'FreeBit4']

        '''
        The control register has 8 bits, with the following specs:

        0 - Active/Inactive
        1 - Reboot
        2 - Direction (1f, 0r)
        3 - Override
        4 - Unused
        5 - Unused
        6 - Unused
        7 - Unused
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
