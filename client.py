import socket

serverip = '192.168.0.54'
port = 8888
buffsize = 4096


for i in range(10):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))

    data = input('Send to server :')
    server.send(data.encode('utf-8'))

    data_server = server.recv(buffsize).decode('utf-8')
    print('Data from server :', data_server)
    server.close()
