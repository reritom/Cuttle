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
        self.max_angle = 45 # degrees
        self.length = 20 # centimetres
        self.previous_bit = 0
        self.position = 0

    def runRound(self, bit, delta):
        '''
            Calculate the new position using the previous bit and the delta, and return the new position
        '''
        if Config.FinType == 'Linear':
            self.linearCalc(delta)
        elif Config.FinType == 'Exp':
            pass

        self.previous_bit = bit

        return self.position

    def linearCalc(self, delta):
        prop_rate = self.max_angle / self.propagation_time
        if self.position <= self.max_angle:
            self.position = self.position + self.previous_bit * delta * prop_rate
            self.position = self.position if self.position < self.max_angle else self.max_angle


    def expCalc(self):
        pass
