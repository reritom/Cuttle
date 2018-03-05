'''
  Fins are used to make up the tracks.
  It has two binary inputs
  The output is the position and is time dependent.
  If both inputs are 1, it will break
  If both are zero, its neutral
  If it is XOR, the fin will either move up or down
'''
class Fin():
    def __init__(self):
        self.propagation_time = 1 # seconds
        self.propagation_type = 'Linear' # 'Exp'
        self.max_angle = 45 # degrees
        self.length = 20 # centimetres
        pass

    def runRound(self):
        pass
