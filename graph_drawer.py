import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TKGraph(FigureCanvasTkAgg):
    def __init__(self, master):
        self.acceleration_data = [[],[],[]]
        self.rotation_data = [[],[],[]]
        self.time = []
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(self.acceleration_data[0], self.time, label='x')
        ax1.plot(self.acceleration_data[1], self.time, label='y')
        ax1.plot(self.acceleration_data[2], self.time, label='z')
        ax1.legend()
        ax1.set_ylabel("acceleration")
        ax2.plot(self.rotation_data[0], self.time, label='x')
        ax2.plot(self.rotation_data[1], self.time, label='y')
        ax2.plot(self.rotation_data[2], self.time, label='z')
        ax2.legend()
        ax2.set_ylabel("rotation")
        ax2.set_xlabel("time (s)")
        super().__init__(figure=fig, master=master)
    
    def start_recording(self):
        pass

    def stop_recording(self):
        pass

    def add_point(self, time, acceleration, rotation):
        pass

    def clear_graph(self):
        pass
    