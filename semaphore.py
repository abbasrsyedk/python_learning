import multiprocessing 
import time
semaphore = multiprocessing.Semaphore()

def fun1():
    time = 0
    while time<10:
        semaphore.acquire()
        print(1)
        semaphore.release()
        time += 1
    else:
        print("fun1 is ended")
def fun2():
    time = 0
    while time<5:
        semaphore.acquire()
        print(2)
        semaphore.release()
        time += 1
    else:
        print("fun2 is ended")

if __name__ == '__main__': 

    p1 = multiprocessing.Process(target=fun1) 
    p2 = multiprocessing.Process(target=fun2) 

    p1.start()
    p2.start()


# t = threading.Thread(target = fun1)
# t.start()
# t2 = threading.Thread(target = fun2)
# t2.start()