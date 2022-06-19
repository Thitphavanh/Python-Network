from tkinter import *
from tkinter import ttk, messagebox
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



GUI = Tk()
GUI.title('[2] In')
GUI.geometry('300x400')
FONT = (20)

label = Label(GUI,text='BRAND',font=FONT)
label.pack()

v_brand = StringVar()
entry1 = ttk.Entry(GUI, textvariable=v_brand,font=FONT)
entry1.pack()

label = Label(GUI,text='COLOR',font=FONT)
label.pack()

v_color = StringVar()
entry2 = ttk.Entry(GUI, textvariable=v_color,font=FONT)
entry2.pack()



label = Label(GUI,text='PLATE',font=FONT)
label.pack()

v_plate = StringVar()
entry3 = ttk.Entry(GUI, textvariable=v_plate,font=FONT)
entry3.pack()


label = Label(GUI,text='CAR CARD',font=FONT)
label.pack()

v_card = IntVar()
v_card.set(1001) # start card number
entry4 = ttk.Entry(GUI, textvariable=v_card,font=FONT)
entry4.pack()

def carIn():
	information = {'brand': {'q': 'Brand : ', 'value': ''},
				   'color': {'q': 'Color : ', 'value': ''},
				   'plate': {'q': 'Plate : ', 'value': ''},
				   'card': {'q': 'Card : ', 'value': ''}}

	timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	brand = v_brand.get()
	color = v_color.get()
	plate = v_plate.get()
	card = str(v_card.get())


	information['brand']['value'] = brand
	information['color']['value'] = color
	information['plate']['value'] = plate
	information['card']['value'] = card

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
	print('----------------------------')

	v_brand.set('')
	v_color.set('')
	v_plate.set('')
	newcard = v_card.get() + 1
	v_card.set(newcard)


button1 = ttk.Button(GUI,text='CAR IN',command=carIn)
button1.pack(ipadx=20,ipady=5,pady=50)








GUI.mainloop()
