class Wave():
    def __init__(self):
        self.wave = []
        self.pulse_size = 100 # Percent
        self.stage = 0 # Value between 0 and the size of the wave

    def setSize(self, size):
        '''
            Set how many bits long the wave is
            (needs to be even)
        '''
        if size%2 != 0:
            print("Invalid wave size")
            raise Exception
        else:
            self.size = size

    def setPulseWidth(self, percent=100):
        '''
            Set the pulse percentage
        '''
        self.pulse_size = percent

    def createWave(self):
        '''
            This method creates the wave
        '''
        # Number of bits in half a wave
        halfwave = int(self.size / 2)

        # How many bits are active at a time in the halfwave
        halfwave_bits = int(halfwave * self.pulse_size / 100) + (halfwave % (self.pulse_size / 100) > 0)

        # Create an array representing the halfwave
        half_array = [0 for i in range(halfwave)]

        # Add the active bits
        for index, bit in enumerate(range(halfwave_bits)):
            half_array[index] = 1

        # Create the other half
        other_half = [0 for i in range(halfwave)]
        for index, bit in enumerate(half_array):
            if bit == 1:
                other_half[index] = -1

        # Merge them both
        self.wave.extend(half_array)
        self.wave.extend(other_half)

        print("Created wave: " + str(self.wave))

    def getTrite(self):
        '''
            Return the current bit (-1,0,1) and increment the wave
        '''
        print("Getting trite, stage is " + str(self.stage) + " length is " + str(len(self.wave)))
        if self.stage < len(self.wave):
            trite = self.wave[self.stage]
            self.stage = self.stage + 1
            return trite
        else:
            self.stage = 0
            trite = self.wave[self.stage]
            self.stage = self.stage + 1
            return trite
