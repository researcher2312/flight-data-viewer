import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from network_receiver import SensorData


class TKGraph(FigureCanvasTkAgg):
    def __init__(self, master):
        self.recording = False
        self.data_queue = []
        self.acceleration_data = [[] for _ in range(3)]
        self.rotation_data = [[] for _ in range(3)]
        self.time = []
        fig, (self.ax1, self.ax2) = plt.subplots(2, 1, sharex=True)
        labels = ["x", "y", "z"]
        for i in range(3):
            self.ax1.plot(self.time, self.acceleration_data[i], label=labels[i])
            self.ax2.plot(self.time, self.rotation_data[i], label=labels[i])

        self.lines_acceleration = self.ax1.get_lines()
        self.lines_rotation = self.ax2.get_lines()
        self.ax1.legend()
        self.ax2.legend()
        self.ax1.set_ylabel("acceleration")
        self.ax2.set_ylabel("rotation")
        self.ax2.set_xlabel("time (s)")
        self.ax1.set_xlim((0, 20))
        self.ax1.set_ylim(0, 10)
        self.ax2.set_ylim(0, 10)
        super().__init__(figure=fig, master=master)
        self.animation = FuncAnimation(fig, self.update, interval=100)

    def start_recording(self):
        self.animation.resume()

    def stop_recording(self):
        self.animation.pause()

    def add_point(self, new_data: SensorData):
        self.time.append(new_data.time)
        for j in range(3):
            self.acceleration_data[j].append(new_data.acceleration[j])
            self.rotation_data[j].append(new_data.rotation[j])

    def update(self, i):
        while len(self.data_queue) > 0:
            new_data = self.data_queue.pop(0)
            self.time.append(new_data.time / 1000)
            for j in range(3):
                self.acceleration_data[j].append(new_data.acceleration[j])
                self.rotation_data[j].append(new_data.rotation[j])

        if self.time:
            for j in range(3):
                self.lines_acceleration[j].set_data(
                    self.time, self.acceleration_data[j]
                )
                self.lines_rotation[j].set_data(self.time, self.rotation_data[j])

        # self.fig.gca().relim()
        # self.fig.

    def clear_graph(self):
        pass
