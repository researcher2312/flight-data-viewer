import customtkinter as cti

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

        self.buttonRecord = cti.CTkButton(
            master=self, command=self.record_button_callback, text="Record"
        )
        self.buttonRecord.grid(row=2, column=4, padx=10, pady=20, sticky="ew")

        self.network_receiver = NetworkReceiver()

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
        pass

    def close_application(self):
        self.destroy()
        quit()


if __name__ == "__main__":
    app = App()
    app.mainloop()
