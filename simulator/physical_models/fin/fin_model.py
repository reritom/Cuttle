from config import Config

class FinModel():
    '''
        A fin takes a trite input (1, 0 , -1) and uses it to either exponentially
        or linearly calculate the position of the fin using the time delta
    '''
    def __init__(self):
        self.propagation_time = 1 # seconds taken to move from 0-max_angle
        self.propagation_type = 'Linear' # 'Exp'
        self.max_angle = 10 # degrees
        self.length = 20 # centimetres
        self.previous_previous_bit = 0
        self.previous_bit = 0
        self.position = 0

        self.n = 0

    def runRound(self, bit, delta):
        '''
            Calculate the new position using the previous bit and the delta, and return the new position
        '''

        if Config.FinType == 'Linear':
            self.linearCalc(delta, bit)
        elif Config.FinType == 'Exp':
            pass

        self.previous_previous_bit = self.previous_bit
        self.previous_bit = bit

        self.n += 1

        return self.position

    def linearCalc(self, delta, bit):
        '''
        if self.previous_bit > 0:
            self.position = self.max_angle
        elif self.previous_bit < 0:
            self.position = - self.max_angle
        else:
            self.position = 0

        '''
        prop_rate = self.max_angle / self.propagation_time



        bit_dydx = (self.previous_bit - self.previous_previous_bit)


        '''
        if self.position <= self.max_angle:
            self.position = self.position + bit_dydx * delta * prop_rate
            if self.position < -self.max_angle:
                self.position = -self.max_angle
            elif self.position > self.max_angle:
                self.position = self.max_angle
        '''
        if self.n < 100:
            self.position = - self.previous_previous_bit
        else:
            self.position = - self.previous_bit

    def expCalc(self):
        pass
