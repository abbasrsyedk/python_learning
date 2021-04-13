import multiprocessing 

def print_fibbonaci(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
    

def print_armstrong(num):
    lower = 0
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
            print(num)
def print_sum_of_naturals(num):
    num = 16
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
    # use while loop to iterate until zero
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)
    

def print_multiplication_table(num):
    
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)

def print_prime(num):
    lower = 0
    upper = 100
    print("Prime numbers between", lower, "and", upper, "are:")
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


if __name__ == '__main__': 

    p1 = multiprocessing.Process(target=print_armstrong, args=(10,)) 

    p2 = multiprocessing.Process(target=print_fibbonaci, args=(10,)) 

    p3 = multiprocessing.Process(target=print_multiplication_table, args=(5,)) 

    p4 = multiprocessing.Process(target=print_sum_of_naturals, args=(7,)) 

    p5 = multiprocessing.Process(target=print_prime, args=(1,)) 

    p1.start() 

    p2.start() 

    p3.start()

    p4.start()

    p5.start()

    p1.join() 

    p2.join() 

    p3.join() 

    p4.join()

    p5.join() 