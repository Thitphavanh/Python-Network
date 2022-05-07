import socket
from datetime import datetime
import csv


#  ----------------CSV----------------
def writeToCsv(data):
	# data = ['Tesla','black','AF1234','1001','2022-05-07 16:01:20']
	with open('2-car-system-in.csv', 'a', newline='', encoding='utf-8') as file:
		file_writer = csv.writer(file)
		file_writer.writerow(data)
	print('csv saved')


# -------------IP Adress-------------
serverip = '192.168.0.54'
port = 8888
buffsize = 4096


while True:
	q = input(
		'[1] - get multiple car information\n[2] - get single car information\n[q] - exit\n>>>')
	if q == '1':
		text = 'location|allcar'
	elif q == '2':
		getcar = 'Enter plate code : '
		text = 'location|{}'.format(getcar)
	elif q == 'q':
		break

	# conntect and send
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.connect((serverip, port))
	server.send(text.encode('utf-8'))
	data_server = server.recv(buffsize).decode('utf-8')
	print('Data from server : ', data_server)
	server.close()


'''

[3]-car-system-location.py
	-   client-1.py
	function
		-   ດຶງຂໍ້ມູນລົດ ຍີ່ຫໍ້ ສີ ປ້າຍທະບຽນ ບັດ ຈາກ [1]
	-   server.py
		-   ບັນທຶກຕຳແໜ່ງໂຊນຂອງລົດໄດ້ 
		-   ສົ່ງຂໍ່ມູນລົດໄປຫາ [4]
'''
