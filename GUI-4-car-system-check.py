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
port = 8899
buffsize = 4096

GUI = Tk()
GUI.title('[4] Check')
GUI.geometry('300x400')

FONT = (20)

label = Label(GUI,text='PLATE',font=FONT)
label.pack()

v_plate = StringVar()
entry1 = ttk.Entry(GUI, textvariable=v_plate,font=FONT)
entry1.pack()

def carCheck():
	plate = v_plate.get()
	text = 'check|'
	text += plate

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

	text = 'CARS BRAND : {}\n\nCARS PLATE : {}\n\nPARKING ZONE : {}'.format(data_list[3],data_list[5],data_list[-2])
	v_result.set(text)


button1 = ttk.Button(GUI,text='CHECK',command=carCheck)
button1.pack(ipadx=20,ipady=5,pady=50)

v_result = StringVar()
v_result.set('------------Result------------')
result1 = Label(GUI,textvariable=v_result,font=(30))
result1.pack()


GUI.mainloop()
