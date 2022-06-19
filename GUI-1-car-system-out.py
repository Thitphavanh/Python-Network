from tkinter import *
from tkinter import ttk, messagebox
import socket
import csv
import uuid
import threading
from datetime import datetime




def calculateCarHour(dt='2022-05-08 12:27:18', first_hour=10000, next_hour=7000):
	# only hour and minute
	convert = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
	now = datetime.now()
	delta = now - convert
	hour = delta.seconds // 3600
	minute = (delta.seconds % 3600) // 60
	print('Parking time: {} Hours {} minutes'.format(hour, minute))
	total = []
	if hour > 1:
		# ຊົ່ວໂມງທຳອິດ
		total.append(first_hour)  # ຊົ່ວໂມງທຳອິດ 20
		total.append((hour - 1) * next_hour)  # ຊົ່ວໂມງຖັດໄປ
	elif hour == 1:
		total.append(first_hour)

	if minute > 15 and hour >= 1:
		total.append(next_hour)
	elif minute > 15 and hour == 0:
		total.append(first_hour)
	elif minute < 15:
		pass

	cal = sum(total)
	print('Car park fee: {} LAK'.format(cal))
	return (hour,minute,cal) # (hour,minute,fee)

	#  ----------------CSV----------------
def writeToCsv(data):
	# data = ['Tesla','black','AF1234','1001','2022-05-07 16:01:20']
	with open('2-car-system-in.csv', 'a', newline='', encoding='utf-8') as file:
		file_writer = csv.writer(file)
		file_writer.writerow(data)
	print('csv saved')

# -------------RUN SERVER-------------
serverip = '192.168.0.54'
port = 8888
buffsize = 4096

car_dict = {}
key_dict = {}


def outServer():
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

		# ມາຈາກໂປຣແກຣມຝຝັ່ງໃດ in / location / check
		source = data.split('|')[0]

		if source == 'in':
			key = str(uuid.uuid1()).split('-')[0]
			car_dict[key] = data.split('|')
			#  add key to value
			car_dict[key].insert(0,key)
			plate = data.split('|')[3]
			print('PLATE : ', plate)
			key_dict[plate] = key

			writeToCsv(data.split('|'))
			# ບັນທຶກຂໍ່ມູນທີ່ໄດ້ຮັບຈາກ [2]
			# write to csv
			client.send('saved'.encode('utf-8'))
			client.close()
		elif source == 'location':
			text = 'out|'
			for k, v in car_dict.items():
				# text += k + '|' ບໍ່ຕ້ອງສົ່ງ key ໄປ ເພາະມີການພິມໃສ່ແລ້ວ
				for dt in v:
					text += dt + '|'

			print('Send to location : ', text)
			client.send(text.encode('utf-8'))
			client.close()
		else:
			pass


GUI = Tk()
GUI.title('[1] Out')
GUI.geometry('300x400')
FONT = (20)

label = Label(GUI,text='PLATE',font=FONT)
label.pack()

v_plate = StringVar()
entry1 = ttk.Entry(GUI, textvariable=v_plate,font=FONT)
entry1.pack()

def carOut():
	try:
		data_plate = v_plate.get()
		key = key_dict[data_plate]
		print('RESULT : ',car_dict[key])
		result = car_dict[key]
		# ['08be1e28', 'in', 'Tesla', 'red', 'SK8899', '1001', '2022-06-19 18:57:46']
		hour, minute, fee = calculateCarHour(result[-1])

		text = 'CARS PLATE : {}\n\nTIME : {} HOURS {} MINUTES\n\nFEE : {} LAK'.format(result[4],hour,minute,fee)
		v_result.set(text)
		del car_dict[key]
		del key_dict[data_plate]
	except:
		messagebox.showinfo('Car was out','Not information')




button1 = ttk.Button(GUI,text='CAR OUT',command=carOut)
button1.pack(ipadx=20,ipady=5,pady=50)


v_result = StringVar()
v_result.set('------------Result------------')
result1 = Label(GUI,textvariable=v_result,font=(30))
result1.pack()




# Start Server
task = threading.Thread(target=outServer)
task.start()

GUI.mainloop()
