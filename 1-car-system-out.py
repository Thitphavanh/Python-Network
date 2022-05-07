import socket


# -------------IP Adress-------------
serverip = '192.168.0.54'
port = 8888
buffsize = 4096


while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((serverip, port))
    server.listen(1)
    print('waiting client...')

    client, addr = server.accept()
    print('connected from : ', add)

    data = client.recv(buffsize).decode('utf-8')
    print('Data from client : ', data)
    # ບັນທຶກຂໍ່ມູນທີ່ໄດ້ຮັບຈາກ [2]
    # write to csv
    client.send('received your message.'.encode('utf-8'))
    client.close()


'''
[1]-car-system-out.py
	-	server.py
	function
		-	ບັນທຶກເວລາ
		-	ຄຳນວນຊົ່ງໂມງຈອດ
		-	ຄຳນວນຄ່າຈອດ
		-	ບັນທຶກຂໍ່ມູນທີ່ໄດ້ຮັບຈາກ [2]
'''
