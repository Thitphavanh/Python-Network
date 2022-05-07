import socket
import csv
import uuid


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

car_dict = {}


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

	source = data.split('|')[0]  # ມາຈາກໂປຣແກຣມຝຝັ່ງໃດ in / location / check

	if source == 'in':
		key = str(uuid.uuid1()).split('-')[0]
		car_dict[key] = data.split('|')

		writeToCsv(data.split('|'))
		# ບັນທຶກຂໍ່ມູນທີ່ໄດ້ຮັບຈາກ [2]
		# write to csv
		client.send('saved'.encode('utf-8'))
		client.close()
	elif source == 'location':
		text = 'out'
		for k, v in car_dict.items():
			text += k + '|'
			for dt in v:
				text += dt + '|'

		print('Send to location : ', text)
		client.send(text.encode('utf-8'))
		client.close()
	else:
		pass


'''
[1]-car-system-out.py
	-	server.py
	function
		-	ບັນທຶກເວລາ
		-	ຄຳນວນຊົ່ງໂມງຈອດ
		-	ຄຳນວນຄ່າຈອດ
		-	ບັນທຶກຂໍ່ມູນທີ່ໄດ້ຮັບຈາກ [2]
'''
