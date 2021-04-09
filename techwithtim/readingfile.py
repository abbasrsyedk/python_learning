file = open('file.txt','r')
#to read the file
f = file.readlines()
#to remove the /n we create a new list
newf = []

for line in f:
    #we dont get the last letter of the last word
    #so we create a if statement to remove the last
    # #last word completely
    if line[-1] == '\n':
        newf.append(line[:-1])
    #this else prints out the last word
    else:
        newf.append(line)

print(newf)