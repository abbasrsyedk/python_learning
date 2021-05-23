from multiprocessing import Queue
from multiprocessing import Process
from time import sleep
from random import randint


#create message queue
q = Queue(2)

def handle():
    while True:
        try:
            #get news
            x,y = q.get(timeout=8)
        except Exception as e:
            print(e)
            break
        else:
            print("%d+%d=%d"%(x,y,x+y))
def request():
    for _ in range(6):
        sleep(randint(1,16))
        x = randint(1,100)
        y = randint(1,100)
        q.put((x,y))#save message

p1 = Process(target=handle)
p2 = Process(target=request)
print("hi1")
p1.start()
print("hi2")
p2.start()
print("hi3")
p1.join()
print("hi4")
p2.join()
print("hi5")

    