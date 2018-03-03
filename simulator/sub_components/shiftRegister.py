class ShiftRegister():
    '''
        Type of list to represent a shift register
        input gets added to the front of the list, all other elements are pushed out.
        The last element gets lost
    '''
    def __init__(self):
        self.register = [0 for i in range(8)]


    def shift(self, bit):
        self.register.insert(0, bit)
        carry_bit = self.register.pop(-1)
        return carry_bit

    def showRegister(self):
        print(self.register)

    def getRegister(self):
        return self.register

def testShiftRegister():
    reg = ShiftRegister()

    bit = 1
    for i in range(15):
        carry = reg.shift(bit)
        reg.showRegister()
        print(carry)
        if bit == 1:
            bit = 0;
        elif bit == 0:
            bit = 1

if __name__ == '__main__':
    testShiftRegister()
