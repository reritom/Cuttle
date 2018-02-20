from shiftRegister import ShiftRegister
import time

class DaisyChain():
    '''
        Multiple shift registers chained together, so the output of the previous is the inut of the next
    '''
    def __init__(self, number):

        self.registers = list()

        for register in range(number):
            self.registers.append(ShiftRegister())

        self.last_carry = 0
        self.input_bit = None

    def shiftBit(self, bit):
        if bit not in [0, 1, None]:
            raise Exception

        if bit in [0, 1]:
            for i in range(len(self.registers)):
                register = self.registers[i]
                carry = register.shift(bit)
                bit = carry
                self.last_carry = carry

        # This loop part needs to be moved out of the component
        else:
            bit = self.last_carry

            for i in range(len(self.registers)):
                register = self.registers[i]
                carry = register.shift(bit)
                bit = carry
                self.last_carry = carry


        return carry

    def getChain(self):
        merged = list()
        for register in self.registers:
            merged.extend(register.getRegister())

        return merged

    def showChain(self, display=None):
        merged = list()
        for register in self.registers:
            merged.extend(register.getRegister())

        if display is None:
            print(merged)
        else:
            new = list()
            for element in merged:
                if element == 1:
                    new.append('0')
                else:
                    new.append(' ')

            print(new)

    def runRound(self):
        if self.input_bit is not None:
            #Shift bit
            self.input_bit = None


def testDaisyChain():
    daisy = DaisyChain(3)

    bit = 1
    for i in range(15):
        for n in range(3):
            carry = daisy.shiftBit(bit)
            daisy.showChain(display=1)
            time.sleep(0.5)


        if bit == 1:
            bit = 0;
        elif bit == 0:
            bit = 1

    print("Maintenance start")

    bit = None

    for i in range(15):
        daisy.shiftBit(bit)
        daisy.showChain(display=1)
        time.sleep(0.5)

if __name__ == '__main__':
    testDaisyChain()
