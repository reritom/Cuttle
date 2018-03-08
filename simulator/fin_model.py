from config import Config
'''
  Fins are used to make up the tracks.
  It has two binary inputs
  The output is the position and is time dependent.
  If both inputs are 1, it will break
  If both are zero, its neutral
  If it is XOR, the fin will either move up or down
'''
class FinModel():
    def __init__(self):
        self.propagation_time = 1 # seconds taken to move from 0-max_angle
        self.propagation_type = 'Linear' # 'Exp'
        self.max_angle = 10 # degrees
        self.length = 20 # centimetres
        self.previous_bit = 0
        self.position = 0

    def runRound(self, bit, delta):
        '''
            Calculate the new position using the previous bit and the delta, and return the new position
        '''
        if Config.FinType == 'Linear':
            self.linearCalc(delta, bit)
        elif Config.FinType == 'Exp':
            pass

        self.previous_bit = bit

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



        bit_dydx = (bit - self.previous_bit)

        if self.position <= self.max_angle:
            self.position = self.position + bit_dydx * delta * prop_rate
            if self.position < -self.max_angle:
                self.position = -self.max_angle
            elif self.position > self.max_angle:
                self.position = self.max_angle


    def expCalc(self):
        pass
