import bluetooth


class BluetoothReceiver:
    def __init__(self):
        self.available_devices = []
        self.connected_device = None
        self.sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

    def discover_devices(self):
        try:
            self.available_devices = bluetooth.discover_devices()
        except OSError:
            return "No bluetooth hardware"
        except:
            return "error"
        else:
            for dev in self.available_devices:
                print(f"{dev}: {bluetooth.lookup_name(dev)}")
                services = bluetooth.find_service(address=dev)
                for i in services:
                    print(i)

    def connect_to_device(self):
        bd_addr = "01:23:45:67:89:AB"
        port = 0x1001
        self.sock.connect((bd_addr, port))
        self.sock.send("hello!!")
        self.sock.close()
