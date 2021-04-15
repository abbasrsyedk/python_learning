try:
    f = open('testfile','r')
    f.write("write a test line")
except TypeError:
    print("There is a type error")
except OSError:
    print("OS error")
except:
    print("All other exceptions")
finally:
    print("I always run")
