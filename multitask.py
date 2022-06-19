import threading
import time


def Driving():
    # 10 second
    for i in range(10):
        print('ກຳລັງຂັບລົດ...', i)
        time.sleep(1)


def Meeting():
    for i in range(10):
        print('ກຳລັງປະຊຸມ...', i)
        time.sleep(0.5)


t1 = time.time()
# --------------------Normal--------------------

# Driving()
# Meeting()

# --------------------Parallel--------------------

task1 = threading.Thread(target=Driving)
task2 = threading.Thread(target=Meeting)

print(time.time())
task1.start()
print(time.time())
task2.start()


# ເມື່ອເຮັດວຽກແລ້ວໆ ໃຫ້ຫຍຸດຖ້າໜ່ອຍໜຶ່ງ
task1.join()
task2.join()

t2 = time.time()
print('Time : ', t2 - t1)
