from trackDriver import TrackDriver
from constructorObjects.driverCommandRegister import DriverCommandRegister
from constructorObjects.driverSpeedRegister import DriverSpeedRegister

class TrackManager():
    '''
        This class parses a command which is split and sent to both the portside and starboard TrackDrivers
    '''
    def __init__(self):
        self.incomingSerial = None
        self.previousSerial = None
        self.trackDrivers = {'Portside': TrackDriver(name='Portside'),
                             'Starboard': TrackDriver(name='Starboard')}


    def parseSerial(self):
        '''
            Parse the serial input
            Message format: str "XXYYY"
            FS, FL, FR
            RS, RL, RR
            TR, TR
            OX
        '''
        # Split the message by ':'
        commands = self.incomingSerial.split(':')

        for this_command in commands:
            # Starport commands
            if this_command.startswith('S'):
                print("Message received for Starboard driver")
                command_register, speed_register = self.createRegisters(this_command)
                self.trackDrivers['Starboard'].setCommand(command_register.getBinary())
                self.trackDrivers['Starboard'].setSpeed(speed_register.getBinary())
                self.trackDrivers['Starboard'].setInterrupt()

            # Portside commands
            if this_command.startswith('P'):
                print("Message received for Portside driver")
                command_register, speed_register = self.createRegisters(this_command)
                self.trackDrivers['Portside'].setCommand(command_register.getBinary())
                self.trackDrivers['Portside'].setSpeed(speed_register.getBinary())
                self.trackDrivers['Portside'].setInterrupt()


    def createRegisters(self, command):
        '''
            This receives a command and converts it into the command and speed registers
        '''
        # Default to 0000000
        command_register = DriverCommandRegister()
        speed_register = DriverSpeedRegister()

        # Parse the speed
        cutspeed = command[2:]
        speed = int(cutspeed[:3])

        if speed == 0:
            return command_register, speed_register
        else:
            command_register.setActive()
            speed_register.setSpeed(speed)

        # Check that the second character is a valid command
        if command[1] not in ['F', 'O', 'R']:
            print("Invalid command second char")
            raise Exception
        else:
            if command[1] == 'F':
                command_register.setDirection()
            elif command[1] == '0':
                command_register.setOverride()

        return command_register, speed_register


    def runRound(self):
        '''
            This method processes the current round in the loop
        '''
        if self.incomingSerial is not None:
            if self.incomingSerial != self.previousSerial:
                print("New incoming message detected")
                self.parseSerial()
                self.previousSerial = self.incomingSerial
            self.incomingSerial = None
