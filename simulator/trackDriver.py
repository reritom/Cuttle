from sub_components.daisyChain import DaisyChain
from constructor_objects.driverCommandRegister import DriverCommandRegister
from constructor_objects.driverSpeedRegister import DriverSpeedRegister
from constructor_objects.wave import Wave
from config import CONFIG
import copy

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
        self.time_sls = 0 # Time since last shift in microseconds

        # Previous command information
        self.status = 0
        self.direction = 'Fwd' # Default forward
        self.speed = 100 # Somewhat arbritrary

        # Speed is inversely mapped to the time taken between shifting out the new array
        '''
        speed_downscale = (self.speed / 5) # Typical range of 0-20
        time_between_shifts = (1 second / speed_downscale)*1000 to convert to milliseconds
        '''

        # Number of bits until the bit flips
        self.frequency = 2 # Wave size is twice the frequency

        # The waveform to be shifted
        self.wave = Wave()
        self.wave.createWave()

        # Two daisy chains
        self.daisies = {'Skyward': DaisyChain(number=CONFIG['DaisyChainSize']),
                        'Downward': DaisyChain(number=CONFIG['DaisyChainSize'])}

        # For storing the values of the daisies
        self.daisy_arrays = {'Skyward': [0 for i in range(CONFIG['DaisyChainSize'] * 8)],
                             'Downward': [0 for i in range(CONFIG['DaisyChainSize'] * 8)]}

        self.trit_array = [0 for i in range(CONFIG['DaisyChainSize'] * 8)]

    def runRound(self, delta):
        if self.interrupt is not None:
            #Do stuff
            print(self.name)
            print("received: " + str(self.command_register.getBinary()))
            self.parseCommand()
            self.interrupt = None
            self.time_sls = 0
        else:
            pass

        if self.status == 0:
            return copy.deepcopy(self.daisy_arrays['Skyward']), copy.deepcopy(self.daisy_arrays['Downward'])


        self.time_sls += delta
        if self.time_sls < (1/(self.speed)):
            #print("Time since last shift is ..")
            return copy.deepcopy(self.daisy_arrays['Skyward']), copy.deepcopy(self.daisy_arrays['Downward'])

        trite = self.wave.getTrite()

        if self.direction == 'Fwd': # forward
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

        elif self.direction == 'Rev':
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

        elif self.direction == 'Flt':
            # Inject two same bits in the centre
            center_element = int(len(self.daisy_arrays['Skyward']) / 2)

            if trite == 1:
                self.daisy_arrays['Skyward'].insert(center_element, trite)
                self.daisy_arrays['Skyward'].insert(center_element, trite)
                self.daisy_arrays['Downward'].insert(center_element, 0)
                self.daisy_arrays['Downward'].insert(center_element, 0)
            elif trite == 0:
                self.daisy_arrays['Skyward'].insert(center_element, 0)
                self.daisy_arrays['Skyward'].insert(center_element, 0)
                self.daisy_arrays['Downward'].insert(center_element, 0)
                self.daisy_arrays['Downward'].insert(center_element, 0)
            elif trite == -1:
                self.daisy_arrays['Skyward'].insert(center_element, 0)
                self.daisy_arrays['Skyward'].insert(center_element, 0)
                self.daisy_arrays['Downward'].insert(center_element, trite)
                self.daisy_arrays['Downward'].insert(center_element, trite)

            # Pop the beginning and end bits
            carry_bit_sky = self.daisy_arrays['Skyward'].pop(0)
            carry_bit_down = self.daisy_arrays['Downward'].pop(0)

            carry_bit_sky = self.daisy_arrays['Skyward'].pop(-1)
            carry_bit_down = self.daisy_arrays['Downward'].pop(-1)
            '''
            if self.name == "Starboard":
                print(self.daisy_arrays['Skyward'])
            '''
        elif self.direction == 'Ntl':
            # Neutral direction means no movement, end round
            return

        else:
            print("Unsupported direction: " + self.direction)
            raise Exception

        self.time_sls = 0
        return copy.deepcopy(self.daisy_arrays['Skyward']), copy.deepcopy(self.daisy_arrays['Downward'])

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
        if self.status == 0:
            return


        if self.command_register.getReboot() == 1:
            # TODO
            # Run reset of the daisy chains
            # Do a "If reboot, at end of parse command, run reboot func"
            return

        if self.command_register.getDefault() == 1:
            # This is a speed change command
            # Ignore other mode change bits
            # Get the direction
            self.direction = self.command_register.getDirection()
            self.speed = self.speed_register.getSpeed()

            if self.speed == 0:
                self.speed = 1
            return

        mode =  self.command_register.getMode()
        if mode == 'OM':
            # Override ignores direction changes, it is applied to the current direction
            # Read speed, treat them as multipliers, run override routine, return to loop
            override = self.speed_register.getSpeed() / 50 # Value between 0-2
            self.speed = self.speed*override
            return
        elif mode == 'FC':
            # Its a frequency change
            frequency = self.speed_register.getSpeed()
            if frequency > 10:
                print("Frequency too high, using 10f instead")
                frequency = 10
            self.frequency = frequency
            self.wave.setSize(self.frequency*2)
            self.wave.createWave()
            return
        elif mode == 'WC':
            # Wave shape change
            # Read speed as a pwm type
            pwm_percent = self.speed_register.getSpeed()
            self.wave.setPulseWidth(pwm_percent)
            self.wave.createWave()
            return
        else:
            print("Not yet supported mode: " + mode)
            raise Exception
