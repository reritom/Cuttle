from simulationDriver import SimulationDriver

class logAnimator():
    def __init__(self):
        self.logs = []
        pass

    def runSimulation(self):
        sim = SimulationDriver(duration=100, sampling=0.04)
        sim.addEvent(5, "ST050:PR100") #Frequency (will default to 10 bit half wave size)
        sim.addEvent(10, "SW050") #50% pwm
        sim.addEvent(15, "SR050") #Change direction and reduce speed
        sim.runSimulation()

        self.logs = sim.getLogs()

    def animateLogs(self):
        '''
            This method animates the simulation logs
        '''
        pass
