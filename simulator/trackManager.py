from trackDriver import TrackDriver
from constructorObjects.driverControl import DriverControl

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
        '''
        if self.incomingSerial[:2] == 'FS':
            speed = self.incomingSerial[2:]
            speed = speed[:4]

            portsideControl = DriverControl()
            portsideControl.setActive()
            portsideControl.setSpeed(speed)
            portsideCommand = portsideControl.getBinary()
            self.trackDrivers['Portside'].setCommand(portsideCommand)
            self.trackDrivers['Portside'].setInterrupt()

            starboardControl = DriverControl()
            starboardControl.setActive()
            starboardControl.setSpeed(speed)
            starboardCommand = starboardControl.getBinary()
            self.trackDrivers['Starboard'].setCommand(starboardCommand)
            self.trackDrivers['Starboard'].setInterrupt()


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
