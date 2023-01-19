import customtkinter as cti
import random

from graph_drawer import TKGraph
from network_receiver import NetworkReceiver


class App(cti.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.title("Flight data viewer 0.1")
        self.minsize(600, 200)
        self.protocol("WM_DELETE_WINDOW", self.close_application)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2, 3, 4), weight=0)
        self.grid_columnconfigure((0, 5), weight=1)

        self.chart = TKGraph(master=self)
        self.chart.get_tk_widget().grid(
            row=0, column=0, columnspan=6, padx=20, pady=(20, 0), sticky="nsew"
        )

        self.label = cti.CTkLabel(master=self)
        self.label.grid(
            row=1, column=0, columnspan=6, padx=20, pady=(20, 0), sticky="nsew"
        )

        self.combobox = cti.CTkOptionMenu(
            master=self, command=self.option_menu_callback, values=["no devices"]
        )
        self.combobox.grid(row=2, column=1, padx=10, pady=20, sticky="ew")

        self.button_search = cti.CTkButton(
            master=self, command=self.search_button_callback, text="Search"
        )
        self.button_search.grid(row=2, column=2, padx=10, pady=20, sticky="ew")

        self.buttonConnect = cti.CTkButton(
            master=self, command=self.connect_button_callback, text="Connect"
        )
        self.buttonConnect.grid(row=2, column=3, padx=10, pady=20, sticky="ew")

        self.button_record = cti.CTkButton(
            master=self, command=self.record_button_callback, text="Record"
        )
        self.button_record.grid(row=2, column=4, padx=10, pady=20, sticky="ew")

        self.network_receiver = NetworkReceiver(data_store=self.chart.data_queue)
        # self.chart.animation.pause()

        self.create_mock_measurements()

    def option_menu_callback(self, choice):
        print(choice)

    def search_button_callback(self):
        connection_result = self.network_receiver.discover_devices()
        self.label.configure(text=connection_result)
        print(connection_result)
        self.combobox.configure(values=self.network_receiver.available_devices)

    def connect_button_callback(self):
        pass

    def record_button_callback(self):
        if not self.chart.recording:
            self.button_record.configure(text="Recording")
            self.chart.start_recording()
            self.update()
        else:
            self.chart.stop_recording()
            self.button_record.configure(text="Record")

    def update(self):
        if self.chart.recording:
            print("henlo")
            self.after(1000, self.update)

    def close_application(self):
        self.destroy()
        quit()

    def create_mock_measurements(self):
        random_time = random.randrange(20, 200)
        self.network_receiver.create_mock_data(random_time)
        self.after(random_time, self.create_mock_measurements)


if __name__ == "__main__":
    app = App()
    app.mainloop()
