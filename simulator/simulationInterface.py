from simulationDriver import SimulationDriver
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class logAnimator():
    def __init__(self):
        self.logs = []
        print("In init")

    def runSimulation(self):
        print("Running sim")
        sim = SimulationDriver(duration=20, sampling=0.04)
        sim.addEvent(5, "ST050:PR100") #Frequency (will default to 10 bit half wave size)
        sim.addEvent(10, "SW050") #50% pwm
        sim.addEvent(15, "SR050") #Change direction and reduce speed
        #sim.addEvent(0, "SM050") # Float movement
        sim.runSimulation()
        self.logs = sim.getLogs()

    def animateLogs(self):
        '''
            This method animates the simulation logs
        '''
        print("Animating logs")
        self.frame_count = 0

        # First set up the figure, the axis, and the plot element we want to animate
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 3*8), ylim=(-2, 2))
        self.line, = ax.plot([], [], lw=2)

        # initialization function: plot the background of each frame


        # animation function.  This is called sequentially


        # call the animator.  blit=True means only re-draw the parts that have changed.
        anim = animation.FuncAnimation(fig, self.animate, init_func=self.init,
                               frames=len(self.logs), interval=40, blit=True)

        plt.show()
        '''
        for log in self.logs:
            time = log['time']
            PortsideSky = log['PortsideSky']
            PortsideDown = log['PortsideDown']
            StarboardSky = log['StarboardSky']
            StarboardDown = log['StarboardDown']
            #print(time)
            print(PortsideSky)
            print(PortsideDown)
            print(StarboardSky)
            print(StarboardDown)
            print("..")

        #print(self.logs)
        '''

    def animate(self, i):
        y = self.logs[i]['StarboardSky']
        x = [i for i in range(24)]
        self.line.set_data(x, y)
        return self.line,

    def init(self):
        self.line.set_data([], [])
        return self.line,

if __name__ == '__main__':
    ani = logAnimator()
    ani.runSimulation()
    ani.animateLogs()
