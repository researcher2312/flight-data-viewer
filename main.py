import customtkinter as cti


class App(cti.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x300")
        self.title("Flight data viewer 0.1")
        self.minsize(600, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2, 3), weight=0)
        self.grid_columnconfigure((0, 4), weight=1)



        self.graph = cti.CTkFrame(master=self)
        self.graph.grid(row=0, column=0, columnspan=5, padx=20, pady=(20, 0), sticky="nsew")
        self.frame = cti.CTkLabel(master=self)
        self.frame.grid(row=1, column=0, columnspan=5, padx=20, pady=(20, 0), sticky="nsew")

        self.combobox = cti.CTkOptionMenu(master=self, values=["Sample text 1", "Text 2"])
        self.combobox.grid(row=2, column=1, padx=20, pady=20, sticky="ew")
        self.buttonConnect = cti.CTkButton(master=self, command=self.button_callback, text="Connect")
        self.buttonConnect.grid(row=2, column=2, padx=20, pady=20, sticky="ew")
        self.buttonRecord = cti.CTkButton(master=self, command=self.button_callback, text="Record")
        self.buttonRecord.grid(row=2, column=3, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()