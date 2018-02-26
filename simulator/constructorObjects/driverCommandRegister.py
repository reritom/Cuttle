class DriverCommandRegister(object):
    '''
        This class is used for creating an 8 bit binary message to shift to the driver
        representing commands
    '''
    def __init__(self):
        self.status = False
        self.control_bits = {'Active': 0,
                            'Reboot': 0,
                            'Default': 1,
                            'Mode_b0': 0,
                            'Mode_b1': 0,
                            'Direction_b0': 0,
                            'Direction_b1': 0,
                            'FreeBit1': 0}

        self.bit_order = ['Active',
                          'Reboot',
                          'Default',
                          'Mode_b0',
                          'Mode_b1',
                          'Direction_b0',
                          'Direction_b1',
                          'FreeBit1']

        '''
        The control register has 8 bits, with the following specs:

        0 - Active/Inactive
        1 - Reboot
        2 - Default
        3 - Mode_b0
        4 - Mode_b1
        5 - Direction_b0 (Neutral 00, Forward 10, Reverse 01, Float 11)
        6 - Direction_b1
        7 - FreeBit1
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

    def setDefault(self):
        '''
            This method sets the default mode
        '''
        self.control_bits['Default'] = 1

    def getDefault(self):
        return self.control_bits['Default']

    def setDirection(self, mode):
        '''
            This method sets the direction bit, 1 for forward, 0 for reverse
        '''
        if mode == 'Fwd':
            self.control_bits['Direction_b0'] = 1
            self.control_bits['Direction_b1'] = 0
        elif mode == 'Rev':
            self.control_bits['Direction_b0'] = 0
            self.control_bits['Direction_b1'] = 1
        elif mode == 'Flt':
            self.control_bits['Direction_b0'] = 1
            self.control_bits['Direction_b1'] = 1
        elif mode == 'Ntl':
            self.control_bits['Direction_b0'] = 0
            self.control_bits['Direction_b1'] = 0
        else:
            print("Incorrect setDirection value")
            raise Exception

    def getDirection(self):
        if self.control_bits['Direction_b0'] == 1 and self.control_bits['Direction_b1'] == 0:
            return 'Fwd'
        elif self.control_bits['Direction_b0'] == 0 and self.control_bits['Direction_b1'] == 1:
            return 'Rev'
        elif self.control_bits['Direction_b0'] == 1 and self.control_bits['Direction_b1'] == 1:
            return 'Flt'
        elif self.control_bits['Direction_b0'] == 0 and self.control_bits['Direction_b1'] == 0:
            return 'Ntl'


    def setMode(self, mode):
        '''
            This method sets the mode
            00 - Speed change (SC)
            01 - Wave change (WC)
            10 - Frequency change (FC)
            11 - Override multiplier (OM)
        '''
        if mode == 'SC':
            self.control_bits['Mode_b0'] = 0
            self.control_bits['Mode_b1'] = 0
        elif mode == 'WC':
            self.control_bits['Mode_b0'] = 0
            self.control_bits['Mode_b1'] = 1
        elif mode == 'FC':
            self.control_bits['Mode_b0'] = 1
            self.control_bits['Mode_b1'] = 0
        elif mode == 'OM':
            self.control_bits['Mode_b0'] = 1
            self.control_bits['Mode_b1'] = 1
        else:
            print("Invalid override mode: " + mode)
            raise Exception

        self.control_bits['Default'] = 0

    def getMode(self):
        if self.control_bits['Mode_b0'] == 0 and self.control_bits['Mode_b1'] == 0:
            return 'SC'
        elif self.control_bits['Mode_b0'] == 0 and self.control_bits['Mode_b1'] == 1:
            return 'WC'
        elif self.control_bits['Mode_b0'] == 1 and self.control_bits['Mode_b1'] == 0:
            return 'FC'
        elif self.control_bits['Mode_b0'] == 1 and self.control_bits['Mode_b1'] == 1:
            return 'OM'

    def getBinary(self):
        '''
            This method returns the binary reprentation of the command
        '''
        return [self.control_bits[i] for i in self.bit_order]

    def setBinary(self, binary_string):
        '''
            This method receives a list 'xxxxxxxx' and parses it into the register model
        '''
        for count, elem in enumerate(self.bit_order):
            self.control_bits[elem] = binary_string[count]
