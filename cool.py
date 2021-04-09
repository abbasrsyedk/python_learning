# def hello():
#     return "Hi Abbas"

# def other(some_def_func):
#     print("othr code runs here")
#     print(some_def_func())

# print(other(hello))


def new_decorator(original_func):

    def wrap_func():
        print("some extra code befre original func")
        original_func()
        print("Some extra code, after original func")
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
#print(decorated_func())

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

print(func_needs_decorator())