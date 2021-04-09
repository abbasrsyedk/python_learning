#.find() , .count() 

string = "Please type something"

print(string.find('a'))
#if you have more than one a it will return the first one

print(string.count("w"))

if string.count(" ") > 0:
    print("not good")
else:
    print("good")