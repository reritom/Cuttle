from simulationDriver import SimulationDriver
from matplotlib import pyplot as plt
from matplotlib import animation
from config import CONFIG
import numpy as np

class logAnimator():
    def __init__(self):
        self.logs = []
        print("In init")

    def runSimulation(self):
        print("Running sim")
        sim = SimulationDriver(duration=60, sampling=0.04)


        sim.addEvent(5, "ST050:PR100") #Frequency (will default to 10 bit half wave size)
        sim.addEvent(10, "SW050") #50% pwm
        sim.addEvent(15, "SR050") #Change direction and reduce speed
        sim.addEvent(20, "SM100") # Float movement
        sim.addEvent(25, "SW010")
        sim.addEvent(30, "SW100")
        sim.addEvent(35, "SF001")


        '''

        for i in range(25):
            string = str(i*4)
            while len(string) < 3:
                string = "0" + string
            sim.addEvent(i, "SF" + string)

        count = 50
        for i in range(25, 0, -1):
            string = str(i*4)
            while len(string) < 3:
                string = "0" + string
            sim.addEvent(count, "SF" + string)
            count = count + 1

        sim.addEvent(15, "ST100")
        '''

        '''
        sim.addEvent(1, "SF050")
        sim.addEvent(5, "ST100")
        '''

        sim.runSimulation()
        self.logs = sim.getLogs()
        self.lines = []

    def animateLogs(self):
        '''
            This method animates the simulation logs
        '''
        print("Animating logs")
        self.frame_count = 0

        # First set up the figure, the axis, and the plot element we want to animate

        '''
        fig = plt.figure()
        ax = plt.axes(xlim=(0, CONFIG['DaisyChainSize']*8), ylim=(-2, 2))

        for i in range(2):
            self.lines.append(ax.plot([], [], lw=2)[0])
        '''

        # initialization function: plot the background of each frame
        fig = plt.figure()
        ax1 = fig.add_subplot(2,1,1)
        ax2 = fig.add_subplot(2,1,2)

        ax1.set_xlim([0, CONFIG['DaisyChainSize']*8])
        ax1.set_ylim([-2, 2])

        ax2.set_xlim([0, CONFIG['DaisyChainSize']*8])
        ax2.set_ylim([-2, 2])


        for i in range(2):
            self.lines.append(ax1.plot([], [], lw=2)[0])

        for i in range(2):
            self.lines.append(ax2.plot([], [], lw=2)[0])
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

        x = [i for i in range(CONFIG['DaisyChainSize'] * 8)]

        starsky_y = self.logs[i]['StarboardSky']
        self.lines[0].set_data(x, starsky_y)

        stardown_y = [i for i in self.logs[i]['StarboardDown']]
        self.lines[1].set_data(x, stardown_y)

        portsky_y = self.logs[i]['PortsideSky']
        self.lines[2].set_data(x, portsky_y)

        portdown_y = [i for i in self.logs[i]['PortsideDown']]
        self.lines[3].set_data(x, portdown_y)

        return self.lines

    def init(self):
        for line in self.lines:
            line.set_data([],[])
        return self.lines

if __name__ == '__main__':
    ani = logAnimator()
    ani.runSimulation()
    ani.animateLogs()
