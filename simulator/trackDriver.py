from subComponents.daisyChain import DaisyChain
from constructorObjects.driverCommandRegister import DriverCommandRegister
from constructorObjects.driverSpeedRegister import DriverSpeedRegister

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
            pass

        '''
        if self.direction == 1: # forward
            previous = self.trit_array[0]

        else:
            previous = self.trit_array[-1]

        '''

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

        self.reboot =  self.command_register.getReboot() == 1:
            # Run reset of the daisy chains
            return

        if self.command_register.getDirection() != self.direction:
            pass
            # Direction has changed
            # Turn around daisy shift
            # Continue

        if self.command_register.getOverride() == 1:
            pass
            # Treat following speed bits as multipliers

        # Read speed and update
        speed = self.speed_register.getSpeed()
        print("Speed read as " + str(speed))
        pass
