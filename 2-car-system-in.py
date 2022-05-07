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

	# ບັນທຶກຂໍ້ມູນລົດ ຍີ່ຫໍ້ ສີ ປ້າຍທະບຽນ ບັດ
	information = {'brand': {'q': 'Brand : ', 'value': ''},
				   'color': {'q': 'Color : ', 'value': ''},
				   'plate': {'q': 'Plate : ', 'value': ''},
				   'card': {'q': 'Card : ', 'value': ''}}

	timestamp = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
	# data = input('Send to server : ')

	for k, v in information.items():
		d = input(v['q'])
		information[k]['value'] = d

	text = 'in|'  # 'in|' is prefix from car-system-in

	print(information)

	for v in information.values():
		text += v['value'] + '|'

	text += timestamp
	print(text)

	writeToCsv(text.split('|'))

	# conntect and send
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.connect((serverip, port))
	server.send(text.encode('utf-8'))
	data_server = server.recv(buffsize).decode('utf-8')
	print('Data from server : ', data_server)
	server.close()


'''

[2]-car-system-in.py
	-   client-1.py
	function
		-   ບັນທຶກຂໍ້ມູນລົດ ຍີ່ຫໍ້ ສີ ປ້າຍທະບຽນ ບັດ
		-   ບັນທຶກເວລາເຂົ້າ
		-   ສົ່ງໄປຫາ [1]
		-   ບັນທຶກລົງໃນ csv ເຄື່ອງໂຕເອງ
'''
