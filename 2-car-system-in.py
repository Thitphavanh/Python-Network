import socket

# -------------IP Adress-------------
serverip = '192.168.0.54'
port = 8888
buffsize = 4096


while True:
    # server = socket.socket()
    # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # server.connect((serverip, port))

    # ບັນທຶກຂໍ້ມູນລົດ ຍີ່ຫໍ້ ສີ ປ້າຍທະບຽນ ບັດ
    information = {'brand': {'q': 'Brand : ', 'value': ''},
                   'color': {'q': 'Color : ', 'value': ''},
                   'plate': {'q': 'Plate : ', 'value': ''},
                   'card': {'q': 'Card : ', 'value': ''}}

    # timestamp
    # data = input('Send to server : ')

    for k, v in information.items():
        d = input(v['q'])
        information[k]['value'] = d

    print(information)

    # server.send(data.encode('utf-8'))
    # data_server = server.recv(buffsize).decode('utf-8')
    # print('Data from server : ', data_server)
    # server.close()


'''

[2]-car-system-in.py
	-   client-1.py
	function
		-   ບັນທຶກຂໍ້ມູນລົດ ຍີ່ຫໍ້ ສີ ປ້າຍທະບຽນ ບັດ
		-   ບັນທຶກເວລາເຂົ້າ
		-   ສົ່ງໄປຫາ [1]
		-   ບັນທຶກລົງໃນ csv ເຄື່ອງໂຕເອງ
'''
