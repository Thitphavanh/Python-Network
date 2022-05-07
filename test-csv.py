import csv

def writeToCsv(data):
	# data = ['Tesla','black','AF1234','1001','2022-05-07 16:01:20']
	with open('2-car-system-in.csv','a',newline='', encoding='utf-8') as file:
		file_writer = csv.writer(file)
		file_writer.writerow(data)
	print('csv saved')

data = ['Tesla','black','AF1234','1001','2022-05-07 16:01:20']
writeToCsv(data)