import socket
from datetime import datetime
import csv
import threading


#  ----------------Threading Server----------------
plate_dict = {}
# plate_dict = {'ກຄ8888':['14564644','14564544','14564744']}

serverip_location = '192.168.0.54'
port_location = 8888
buffsize_location = 4096


def locationServer():
    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((serverip_location, port_location))
        server.listen(1)
        print('waiting client...')

        client, addr = server.accept()
        print('connected from : ', addr)

        data = client.recv(buffsize_location).decode('utf-8')
        print('Data from client : ', data)

        # data from 4 : data = 'check|ກຄ8888'
        # ມາຈາກໂປຣແກຣມຝຝັ່ງໃດ in / location / check
        source = data.split('|')[0]
        plate = data.split('|')[1]  # 'ກຄ8888'

        if source == 'check':
            # ['in', 'Tesla', 'red', 'AA8888', '1001', '2022-05-08, 11:41:42', '41c83a9c']
            check = plate_dict[plate]
            text = 'location|'
            for c in check:
                text += c + '|'

            client.send(text.encode('utf-8'))
            client.close()
        else:
            client.close()


#  ----------------Run Thread----------------
task = threading.Thread(target=locationServer)
task.start()


#  ----------------CSV----------------
def writeToCsv(data):
    # data = ['Tesla','black','AF1234','1001','2022-05-07 16:01:20']
    with open('2-car-system-in.csv', 'a', newline='', encoding='utf-8') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(data)
    print('csv saved')


#  ----------------Split----------------
def splitRow(datalist, columns=7):
    result = []
    buflist = []
    for i, t in enumerate(datalist, start=1):
        if i % columns == 0:
            buflist.append(t)
            # print(buflist)
            result.append(buflist)
            buflist = []
        else:
            buflist.append(t)
    return result


# -------------IP Adress-------------
serverip = '192.168.0.54'
port = 8888
buffsize = 4096


while True:
    q = input(
        '[1] - get multiple car information\n[2] - get single car information\n[q] - exit\n>>> ')
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
    datalist = data_server.split('|')[1:-1]  # [1:-1] remove prefix and subfix
    for row in splitRow(datalist, 7):
        print(row)
        # ['in', 'Tesla', 'red', 'AA8888', '1001', '2022-05-08, 11:41:42', '41c83a9c']
        plate_dict[row[4]] = row  # ບັນທຶກຂໍ້ມູນຂອງລົດເກັບໄວ້ເປັນ dict
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
