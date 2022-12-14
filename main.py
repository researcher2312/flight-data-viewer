import customtkinter as cti


class App(cti.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("Flight data viewer 0.1")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.frame = cti.CTkFrame(master=self)
        self.frame.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

        self.combobox = cti.CTkOptionMenu(master=self, values=["Sample text 1", "Text 2"])
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.buttonConnect = cti.CTkButton(master=self, command=self.button_callback, text="Connect")
        self.buttonConnect.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        self.buttonRecord = cti.CTkButton(master=self, command=self.button_callback, text="Record")
        self.buttonRecord.grid(row=1, column=2, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()