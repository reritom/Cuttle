from subComponents.daisyChain import DaisyChain
from constructorObjects.driverControl import DriverControl

class TrackDriver():
    '''
        This class reads from the command register and shifts out bits to control the track relays
    '''
    def __init__(self, name):
        # Register for incoming commands from the manager
        self.command_register = DriverControl()

        # Register for outgoing status information
        self.status_register = [0 for i in range(8)]

        # If set, the command register is read and acted on
        self.interrupt = None

        # Used for simulation purposes
        self.name = name

        # Two daisy chains
        self.daisies = {'Skyward': DaisyChain(number=3),
                        'Downward': DaisyChain(number=3)}

        # For storing the values of the daisies
        self.daisy_arrays = {'Skyward': [0 for i in range(3*8)],
                             'Downward': [0 for i in range(3*8)]}

    def runRound(self):
        if self.interrupt is not None:
            #Do stuff
            print(self.name)
            print("received: " + str(self.command_register.getBinary()))
            self.interrupt = None
        else:
            print(self.name)
            print("No interrupt")

    def setInterrupt(self):
        self.interrupt = True

    def setCommand(self, comList):
        self.command_register.setBinary(comList)

    def parseCommand(self):
        '''
            Read each bit to determine the action
        '''
        pass
