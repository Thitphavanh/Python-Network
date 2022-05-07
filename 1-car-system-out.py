import socket
import csv


# -------------IP Adress-------------
serverip = '192.168.0.54'
port = 8888
buffsize = 4096


#  ----------------CSV----------------
def writeToCsv(data):
    # data = ['Tesla','black','AF1234','1001','2022-05-07 16:01:20']
    with open('2-car-system-in.csv', 'a', newline='', encoding='utf-8') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(data)
    print('csv saved')


while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((serverip, port))
    server.listen(1)
    print('waiting client...')

    client, addr = server.accept()
    print('connected from : ', addr)

    data = client.recv(buffsize).decode('utf-8')
    print('Data from client : ', data)
    writeToCsv(data.split('|'))
    # ບັນທຶກຂໍ່ມູນທີ່ໄດ້ຮັບຈາກ [2]
    # write to csv
    client.send('saved'.encode('utf-8'))
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
