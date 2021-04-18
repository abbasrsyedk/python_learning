#18BEC7011_RSK_ABBAS
#importing multiprocessing package
from threading import * 
#import multiprocessing
#initializing semaphore as sema                
sema = Semaphore(3)#GIVE THE VALUE HERE TO SET THE AMOUNT OF THREADS TO RUN AT A GIVEN INSTANCE
#defining functions to run in threads
# counting up from 0 to i        
def print_countup(name):    
    sema.acquire()                
    for i in range(5):
        print('X value is ' , i , ', ', end = '')
        print(name)
    sema.release() 
#sum of natural numbers in the given range
def print_sum_of_naturals(name):
    num = 16
    sema.acquire()
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
    # use while loop to iterate until zero
    while(num > 0):
        
        sum += num
        num -= 1
    print("The sum is", sum,', ', end = '')
    print(name)
    sema.release()
#counting primes in a range 
def print_prime(name):
    lower = 0
    upper = 20
    sema.acquire()
    print("Prime numbers between", lower, "and", upper, "are:")
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print('Prime number is' , num , ', ', end = '')
                print(name)
    sema.release()
#multiplication table for a particular number
def print_multiplication_table(name):
    sema.acquire()
    num = 3
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i, ', ', end = '')
        print(name)
    sema.release()
#function for printing armstrong numbers in the given range
def print_armstrong(name):
    sema.acquire()
    lower = 5
    upper = 200
    for num in range(lower, upper + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            print(num,', ', end = '')
            print(name)
    sema.release()

#initializing the main code to run
if __name__ == '__main__':
    #initializing the multiprocesses for the defined functions
    t1 = Thread(target = print_countup , args = ('Thread-1',))
    t2 = Thread(target = print_prime , args = ('Thread-2',))
    t3 = Thread(target = print_multiplication_table , args = ('Thread-3',))
    t4 = Thread(target = print_sum_of_naturals , args = ('Thread-4',))
    t5 = Thread(target = print_armstrong , args = ('Thread-5',))
    #starting the processes
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

