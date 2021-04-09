# @ operator

def hello(name = 'Abbas'):
    print(" hello function has been executed")

    def greet():
        return '\t This is the greet() func inside hello'

    def welcome():
        return '\t This is welcoeme func insde hello'
    
    # print(greet())
    # print(welcome())

    print("I am going to reutrn a func")

    if name == 'Abbas':
        return greet()
    else:
        return welcome()

print(hello())

#returning a fucntion inside a function



