from multiprocessing import Queue, Process
from time import sleep
from random import randint

q = Queue(6)


def factorial(num):
    factorial = 1
    if num < 0:
        print("factorial doesnot exist for negative nums")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            factorial = factorial*i
        return factorial


def print_sum_of_naturals(num):
    sum = 1
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 1
    while(num > 0):
        sum += num
        num -= 1
        return sum


def handle1():
    while True:
        try:
            num = q.get(timeout=8)
        except Exception as e:
            print(e)
            break
        else:
            print(f"The factorial of {num} is {factorial(num)}")


def handle2():
    while True:
        try:
            num = q.get(timeout=8)
        except Exception as e:
            print(e)
            break
        else:
            print(
                f"The sum of natural numbers is {print_sum_of_naturals(num)}")


def request1():
    for _ in range(3):
        sleep(randint(1, 3))
        num = randint(1, 10)
        q.put((num))


def request2():
    for _ in range(3):
        sleep(randint(1, 3))
        num = randint(1, 20)
        q.put((num))


p1 = Process(target=handle1)
p2 = Process(target=request1)
p3 = Process(target=handle2)
p4 = Process(target=request2)

p1.start()
p2.start()
p3.start()
p4.start()
p1.join()
p2.join()
p3.join()
p4.join()
# 18BEC7011_RSK.ABBAS
