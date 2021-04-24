

def validateuserinput():

 
    choice = input("please enter a number(0-10): ")#fist displaying the user for asking
    
    acceptable_range = range(0,10) #i can checkif the input is in this acceptableval list#by just saying choice in acceptable_val 
    within_range = False
    #two conditions to check 
    #digit or within_range is False
    while choice.isdigit()==False or within_range == False: 
        choice = input("please enter a number(0-10): ")

        if choice.isdigit() == False:#just to inform the user that he is not entering a digit
            print("Sorry bro not a digit")
        #rangecheck
        elif choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("sorry your input is not in range(0-10)")
                within_range = False
                

        

    return int(choice)

print(validateuserinput())

#some_value ='100'
#some_value.isdigit() to check if the string is a digit

