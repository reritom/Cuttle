class DriverSpeedRegister(object):
    '''
        This class is used for creating an 8 bit binary message to shift to the driver
        representing commands
    '''
    def __init__(self):
        self.speed_array = [0 for i in range(8)]

    def setSpeed(self, value):
        '''
            This method receives an int and converts it into an 8 bit list
        '''
        print("In setSpeed")
        bit_list = self.bitConvert(value)
        print("Speed converted to: " + str(bit_list))
        if len(bit_list) > 8:
            print("Speed value greater than 8 bits")
            raise Exception
        else:
            self.speed_array = bit_list

    def getBinary(self):
        '''
            This method returns the binary reprentation of the command
        '''
        return self.speed_array

    def bitConvert(self, number):
        '''
            This method converts and int to a binary list
        '''
        return [int(digit) for digit in bin(number)[2:]] # [2:] to chop off the "0b" part

    def setBinary(self, binary_list):
        '''
            This method receives a string 'xxxxxxxx' and parses it into the register model
        '''
        self.speed_array = binary_list

    def getSpeed(self):
        '''
            This method returns the int value of the stored 8 bit speed value
        '''
        speed_int = 0
        for bit in self.speed_array:
            speed_int = (speed_int << 1) | bit

        return speed_int
