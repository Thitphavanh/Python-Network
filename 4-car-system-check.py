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
port = 8899
buffsize = 4096


while True:
	text = 'check|'
	q = input('Enter plate No. : ')
	text += q

	# conntect and send
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.connect((serverip, port))
	server.send(text.encode('utf-8'))
	data_server = server.recv(buffsize).decode('utf-8')
	print('Data from server : ', data_server)
	data_list = data_server.split('|')
	print('Your car zone : ', data_list[-2])
	server.close()
	print('----------------------------')


'''
[4]-car-system-check.py
	-	client3.py
	function
		-	ດຶງຂໍ້ມູນລົດ ຍີ່ຫໍ້ ສີ ປ້າຍທະບຽນ ບັດ ຈາກ [3]
		-	ດຶງຂໍ່ມູນຕຳແໜ່ງໂຊນຂອງລົດຈາກ [3]
'''
