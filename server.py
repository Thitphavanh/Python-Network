import socket

serverip = '192.168.0.54'
port = 8888
buffsize = 4096


while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((serverip, port))
    server.listen(1)
    print('waiting client...')

    client, add = server.accept()
    print('connected from : ', add)

    data = client.recv(buffsize).decode('utf-8')
    print('Data from client : ', data)
    client.send('received your message.'.encode('utf-8'))
    client.close()
