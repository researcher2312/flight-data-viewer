import socket


class NetworkReceiver:
    def __init__(self):
        self.available_devices = []
        self.connected_device = None
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            raise OSError('Invalid socket')
    
    def discover_devices(self):
        for i in range(256):
            for j in range(256):
                ip = "192.168.%d.%d" % (i, j)
                try:
                    print(socket.gethostbyaddr(ip))
                except:
                    print(f"error at {ip}")
        return True

    # def connect(self):
    #     self.socket.connect((remote_ip , port))
    #     print 'Socket Connected to ' + host + ' on ip ' + remote_ip

# host = 'www.google.com';
# port = 80;

# try:
# 	remote_ip = socket.gethostbyname( host )
# except socket.gaierror:
# 	#could not resolve
# 	print 'Hostname could not be resolved. Exiting'
# 	sys.exit()



#Send some data to remote server
# message = "GET / HTTP/1.1\r\n\r\n"
# try :
# 	#Set the whole string
# 	s.sendall(message)
# except socket.error:
# 	#Send failed
# 	print 'Send failed'
# 	sys.exit()
# print 'Message send successfully'

# #Now receive data
# reply = s.recv(4096)
# print reply

