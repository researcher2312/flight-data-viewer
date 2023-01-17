import socket
import random

class SensorData:
    def __init__(self, time, acceleration, rotation):
        self.time = time
        self.acceleration = acceleration
        self.rotation = rotation

class NetworkReceiver:
    def __init__(self):
        self.available_devices = []
        self.connected_device = None
        self.data_is_available = False
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            raise OSError('Invalid socket')
    
    def discover_devices(self):
        pass
        # for i in range(256):
        #     for j in range(256):
        #         ip = "192.168.%d.%d" % (i, j)
        #         try:
        #             print(socket.gethostbyaddr(ip))
        #         except:
        #             print(f"error at {ip}")
        # return True

    def connect(self):
        pass
        # self.socket.connect((remote_ip , port))
        # print 'Socket Connected to ' + host + ' on ip ' + remote_ip

    def create_mock_data(self, time):
        return SensorData(
            acceleration=random.sample((0, 5),3),
            rotation=random.sample((0, 5),3),
            time=time)


