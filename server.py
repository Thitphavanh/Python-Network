import socket

serverip = '192.168.0.54'
port = 8888

server = socket.socket()

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((serverip,port))

server.listen(1)