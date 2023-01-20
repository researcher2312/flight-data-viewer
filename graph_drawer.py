import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from network_receiver import SensorData


class TKGraph(FigureCanvasTkAgg):
    def __init__(self, master):
        self.recording = False
        self.data_queue = []
        self.sensor_data = pd.DataFrame(
            columns=(
                "time",
                "acceleration_x",
                "acceleration_y",
                "acceleration_z",
                "rotation_x",
                "rotation_y",
                "rotation_z",
            )
        )
        fig, (self.ax1, self.ax2) = plt.subplots(2, 1, sharex=True)
        labels = ["x", "y", "z"]
        for i in range(3):
            self.ax1.plot([], [], label=labels[i])
            self.ax2.plot([], [], label=labels[i])
        self.ax1.legend()
        self.ax2.legend()
        self.ax1.set_ylabel("acceleration")
        self.ax2.set_ylabel("rotation")
        self.ax2.set_xlabel("time (s)")
        self.ax1.set_xlim((0, 20))
        self.ax1.set_ylim(0, 10)
        self.ax2.set_ylim(0, 10)
        super().__init__(figure=fig, master=master)
        self.animation = FuncAnimation(fig, self.update, interval=50, blit=True)

    def start_recording(self):
        self.recording = True
        self.animation.resume()

    def stop_recording(self):
        self.recording = False
        self.animation.pause()

    def add_point(self, new_data: SensorData):
        self.sensor_data.loc[len(self.sensor_data.index)] = [
            new_data.time / 1000,
            new_data.acceleration[0],
            new_data.acceleration[1],
            new_data.acceleration[2],
            new_data.rotation[0],
            new_data.rotation[1],
            new_data.rotation[2],
        ]

    def update(self, i):
        while self.data_queue:
            self.add_point(self.data_queue.pop(0))

        lines_acceleration = self.ax1.get_lines()
        lines_rotation = self.ax2.get_lines()

        if len(self.sensor_data.index):
            for j in range(3):
                lines_acceleration[j].set_data(
                    self.sensor_data.iloc[:, 0], self.sensor_data.iloc[:, j + 1]
                )
                lines_rotation[j].set_data(
                    self.sensor_data.iloc[:, 0], self.sensor_data.iloc[:, j + 4]
                )

        # self.fig.gca().relim()
        # self.fig.
        return lines_acceleration + lines_rotation

    def clear_graph(self):
        pass
