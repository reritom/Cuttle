from subComponents.daisyChain import DaisyChain

class TrackDriver():
    '''
        This class reads from the command register and shifts out bits to control the track relays
    '''
    def __init__(self, name):
        self.command_register = [0 for i in range(8)]
        self.status_register = [0 for i in range(8)]
        self.interrupt = None
        self.name = name
        self.daisy = DaisyChain(number=3)

    def runRound(self):
        if self.interrupt is not None:
            #Do stuff
            print(self.name)
            print(self.daisy.getChain())
            self.interrupt = None
        else:
            print(self.name)
            print("No interrupt")
            print(self.daisy.getChain())

    def setInterrupt(self):
        self.interrupt = True
