from simulationDriver import SimulationDriver
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class logAnimator():
    def __init__(self):
        self.logs = []
        pass

    def runSimulation(self):
        sim = SimulationDriver(duration=20, sampling=1)
        sim.addEvent(5, "ST050:PR100") #Frequency (will default to 10 bit half wave size)
        sim.addEvent(10, "SW050") #50% pwm
        sim.addEvent(15, "SR050") #Change direction and reduce speed
        sim.runSimulation()

        self.logs = sim.getLogs()

    def animateLogs(self):
        '''
            This method animates the simulation logs
        '''
        # First set up the figure, the axis, and the plot element we want to animate
        fig = plt.figure()
        ax = plt.axes(xlim=(0, 24), ylim=(-2, 2))
        self.line, = ax.plot([], [], lw=2)

        # initialization function: plot the background of each frame


        # animation function.  This is called sequentially


        # call the animator.  blit=True means only re-draw the parts that have changed.
        anim = animation.FuncAnimation(fig, self.animate, init_func=self.init,
                               frames=200, interval=20, blit=True)

        plt.show()

        for log in self.logs:
            Time = log[0]
            PortsideSky = log[1]['Portside']['Skyward']
            PortsideDown = log[1]['Portside']['Downward']
            StarboardSky = log[1]['Starboard']['Skyward']
            StarboardSky = log[1]['Starboard']['Downward']
            print(PortsideSky)
        pass

    def animate(self, i):
        print(i)
        x = np.linspace(0, 24)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        self.line.set_data(x, y)
        return self.line,

    def init(self):
        self.line.set_data([], [])
        return self.line,

if __name__ == '__main__':
    ani = logAnimator()
    #ani.runSimulation()
    ani.animateLogs()
