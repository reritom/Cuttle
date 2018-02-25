from subComponents.daisyChain import DaisyChain
from constructorObjects.driverCommandRegister import DriverCommandRegister
from constructorObjects.driverSpeedRegister import DriverSpeedRegister
from constructorObjects.wave import Wave

class TrackDriver():
    '''
        This class reads from the command register and shifts out bits to control the track relays
    '''
    def __init__(self, name):
        # Register for incoming commands from the manager
        self.command_register = DriverCommandRegister()

        # Register for incoming speed commands
        self.speed_register = DriverSpeedRegister()

        # Register for outgoing status information
        self.status_register = [0 for i in range(8)]

        # If set, the command register is read and acted on
        self.interrupt = None

        # Used for simulation purposes
        self.name = name

        # Previous command information
        self.status = 0
        self.direction = 1 #Default forward
        self.speed = 0

        # Number of bits until the bit flips
        self.frequency = 2

        # Trit has 3 states, -1, 0, 1
        self.previous_trit = 0
        self.last_flip = 0
        self.bits_since_command = 0
        self.wave = Wave()

        # Two daisy chains
        self.daisies = {'Skyward': DaisyChain(number=3),
                        'Downward': DaisyChain(number=3)}

        # For storing the values of the daisies
        self.daisy_arrays = {'Skyward': [0 for i in range(3*8)],
                             'Downward': [0 for i in range(3*8)]}

        self.trit_array = [0 for i in range(3*8)]

    def runRound(self):
        if self.interrupt is not None:
            #Do stuff
            print(self.name)
            print("received: " + str(self.command_register.getBinary()))
            self.parseCommand()
            self.interrupt = None
        else:
            pass
            print(self.name)
            print("No interrupt")

        if self.status == 0:
            return

        trite = self.wave.getTrite()

        if self.direction == 1: # forward
            # Prepend bits
            # Pop last bit
            if trite == 1:
                self.daisy_arrays['Skyward'].insert(0, trite)
                self.daisy_arrays['Downward'].insert(0, 0)
            elif trite == 0:
                self.daisy_arrays['Skyward'].insert(0, 0)
                self.daisy_arrays['Downward'].insert(0, 0)
            elif trite == -1:
                self.daisy_arrays['Skyward'].insert(0, 0)
                self.daisy_arrays['Downward'].insert(0, trite)

            carry_bit_sky = self.daisy_arrays['Skyward'].pop(-1)
            carry_bit_down = self.daisy_arrays['Downward'].pop(-1)

        else:
            # Reverse
            # Get bit for each array
            # Append bits to each, pop first from each

            if trite == 1:
                self.daisy_arrays['Skyward'].append(trite)
                self.daisy_arrays['Downward'].append(0)
            elif trite == 0:
                self.daisy_arrays['Skyward'].append(0)
                self.daisy_arrays['Downward'].append(0)
            elif trite == -1:
                self.daisy_arrays['Skyward'].append(0)
                self.daisy_arrays['Downward'].append(trite)

            carry_bit_sky = self.daisy_arrays['Skyward'].pop(0)
            carry_bit_down = self.daisy_arrays['Downward'].pop(0)

        if self.name == "Starboard":
            print("Skyward: " + str(self.daisy_arrays['Skyward']))
            print("Downward: " + str(self.daisy_arrays['Downward']))

    def setInterrupt(self):
        self.interrupt = True

    def setCommand(self, comList):
        print("In driver setCommand, command is " + str(comList))
        self.command_register.setBinary(comList)

    def setSpeed(self, speedList):
        self.speed_register.setBinary(speedList)

    def parseCommand(self):
        '''
            Read each bit to determine the action
        '''
        self.status = self.command_register.getActive()

        self.reboot =  self.command_register.getReboot()
        # Run reset of the daisy chains
        # Do a "If reboot, at end of parse command, run reboot func"


        if self.command_register.getDirection() != self.direction:
            pass
            # Direction has changed
            # Turn around daisy shift
            # Continue

        if self.command_register.getOverride() == 1:
            pass
            # Treat following speed bits as multipliers

        # Read speed and update
        self.speed = self.speed_register.getSpeed()
        print("Speed read as " + str(self.speed))

        # Create the new Wave
        self.wave.setSize(6)
        self.wave.setPulseWidth()
        self.wave.createWave()
