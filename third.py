#asks input untill we provide an interger

def ask_for_int():

    while True:
        try:
            result = int(input("numbrt:"))
        except:
            print("not a number")
            continue
        else:
            print("thank you")
            break
        #finally can be mixed with the else block and 
        #isnt actualy needed
        finally:
            print("end of try?finally")
            print("i will alwasy run")

print(ask_for_int())




