from config import Config

class FinModel():
    '''
        A fin takes a trite input (1, 0 , -1) and uses it to either exponentially
        or linearly calculate the position of the fin using the time delta
    '''
    def __init__(self, name):
        self.propagation_time = Config.PropagationTime # seconds taken to move from 0-max_angle
        self.propagation_type = Config.FinType # 'Exp'
        self.max_angle = Config.MaxAngle # degrees
        self.length = Config.FinLength # centimetres
        self.previous_previous_bit = 0
        self.previous_bit = 0
        self.position = 0
        self.name = name # For sim purposes

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

        return self.position

    def linearCalc(self, delta, bit):
        prop_rate = self.max_angle / self.propagation_time

        gradient = 0

        if self.previous_bit == 0 and self.previous_previous_bit == 0:
            gradient = 0
        elif self.previous_bit == 1 and self.previous_previous_bit == 1:
            gradient = 1
        elif self.previous_bit == -1 and self.previous_previous_bit == -1:
            gradient = -1

        elif self.previous_bit == 0 and self.previous_previous_bit == 1:
            gradient = 1
        elif self.previous_bit == 0 and self.previous_previous_bit == -1:
            gradient = -1
        elif self.previous_bit == 1 and self.previous_previous_bit == 0:
            gradient = -1
        elif self.previous_bit == -1 and self.previous_previous_bit == 0:
            gradient = 1

        elif self.previous_bit == 1 and self.previous_previous_bit == -1:
            gradient = -1
        elif self.previous_bit == -1 and self.previous_previous_bit == 1:
            gradient = 1


        if self.position <= self.max_angle:
            self.position = self.position + gradient * delta * prop_rate
            if self.position < -self.max_angle:
                self.position = -self.max_angle
            elif self.position > self.max_angle:
                self.position = self.max_angle


    def expCalc(self):
        pass
