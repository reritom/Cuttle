from trackDriver import TrackDriver
from constructorObjects.driverControl import DriverControl

class TrackManager():
    '''
        This class parses a command which is split and sent to both the portside and starboard TrackDrivers
    '''
    def __init__(self):
        self.incomingSerial = None
        self.trackDrivers = {'Portside': TrackDriver(name='Portside'),
                             'Starboard': TrackDriver(name='Starboard')}
        self.previousSerial = None
        pass

    def parseSerial(self):
        '''
            Parse the serial input
        '''
        if self.incomingSerial == 'GO':
            portsideCommand = '?'
            #TODO create driverControl for each, then send the command into the driver buffers
            return {'Portside':'FORWARD', 'Starboard':'FORWARD'}


    def driverTransmission(self):
        '''
            This method takes the commands for the drivers and adds them to the input buffers
            It then sets the interrupts
        '''

    def runRound(self):
        '''
            This method processes the current round in the loop
        '''
        if self.incomingSerial is not None:
            if self.incomingSerial != self.previousSerial:
                #Do stuff
                print("New incoming message detected")
                pass


            self.previousSerial = self.incomingSerial
            self.incomingSerial = None
        # If serial, read it, else finish round

        # parse the serial
        pass
