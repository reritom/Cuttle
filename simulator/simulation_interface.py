from simulation_driver import SimulationDriver
from matplotlib import pyplot as plt
from matplotlib import animation
from config import Config
import numpy as np

class logAnimator():
    def __init__(self):
        self.logs = []

    def runSimulation(self):
        '''
            This method creates the simulation object, adds the events,
            runs the simulation, and returns the logs
        '''
        print("Starting simulation")
        sim = SimulationDriver(duration=Config.Duration, sampling=Config.SampleRate / 1000)

        sim.addEvent(0, "SM010:PR100") #Frequency (will default to 10 bit half wave size)
        sim.addEvent(10, "SR005")
        '''
        sim.addEvent(10, "SW050") #50% pwm
        sim.addEvent(15, "SR050") #Change direction and reduce speed
        sim.addEvent(20, "SM100") # Float movement
        sim.addEvent(25, "SW010")
        sim.addEvent(30, "SW100")
        sim.addEvent(35, "SF001")
        '''

        sim.runSimulation()
        self.logs = sim.getLogs()
        self.lines = []

    def plotFin(self):
        '''
            This method plots the position change of a single fin
        '''
        this_fin_position = [log['StarboardFins'][0] for log in self.logs]
        this_fin_state = [log['StarboardTrit'][0] for log in self.logs]
        this_x_axis = [i for i in range(len(this_fin_state))]

        fig = plt.figure()
        ax1 = fig.add_subplot(2,1,1)

        lines = []
        for i in range(2):
            lines.append(ax1.plot([], [], lw=2)[0])

        lines[0].set_data(this_x_axis, this_fin_position)
        lines[1].set_data(this_x_axis, this_fin_state)

        ax1.set_title("Starboard bit 0 progression")
        ax1.set_xlim([0, len(this_x_axis)])
        ax1.set_ylim([-20, 20])

        ax1.lines.extend(lines)

        plt.show()

    def animateLogs(self):
        '''
            This method animates the simulation logs
        '''
        print("Animating logs")

        fig = plt.figure()
        ax1 = fig.add_subplot(2,1,1)
        ax2 = fig.add_subplot(2,1,2)

        ax1.set_xlim([0, Config.DaisyChainSize*8])
        ax1.set_ylim([-20, 20])
        ax1.set_title("Starboard Track")

        ax2.set_xlim([0, Config.DaisyChainSize*8])
        ax2.set_ylim([-20, 20])
        ax2.set_title("Portside Track")

        # Create two lines for ax1
        for i in range(2):
            self.lines.append(ax1.plot([], [], lw=2)[0])

        # Create two lines for ax2
        for i in range(2):
            self.lines.append(ax2.plot([], [], lw=2)[0])


        # Call the animator.  blit=True means only re-draw the parts that have changed.
        anim = animation.FuncAnimation(fig, self.animate, init_func=self.init,
                               frames=len(self.logs), interval=Config.SampleRate, blit=True)

        plt.show()

    def animate(self, i):
        '''
            This method updates each of the log lines
            :param i: an auto-incrementing counter
        '''
        x = [i for i in range(Config.DaisyChainSize * 8)]

        startrit_y = self.logs[i]['StarboardTrit']
        self.lines[0].set_data(x, startrit_y)

        starfins_y = self.logs[i]['StarboardFins']
        self.lines[1].set_data(x, starfins_y)

        porttrit_y = self.logs[i]['PortsideTrit']
        self.lines[2].set_data(x, porttrit_y)

        portfins_y = self.logs[i]['PortsideFins']
        self.lines[3].set_data(x, portfins_y)

        return self.lines

    def init(self):
        for line in self.lines:
            line.set_data([],[])
        return self.lines

if __name__ == '__main__':
    ani = logAnimator()
    ani.runSimulation()
    ani.plotFin()
    #ani.animateLogs()
