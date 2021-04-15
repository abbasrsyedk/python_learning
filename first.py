def add(n1,n2):
    print(n1+n2)

#print(add(1,2))

#number1 = 10

#number2 = input("Please provide a number : ")

#print(add(number1, number2)) type error for the input given is a string

# try:
#     #want to attempt this code 
#     #may have an error
#     result = 10 + 10
#     print(result)
# except:
#     print("hey you arent adding corectly")

try:
    #want to attempt this code 
    #may have an error
    result = 10 + '10'
except:
    print("hey you arent adding corectly")
else:
    print("adding went well")
    print(result)