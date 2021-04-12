def gen_fibon(n):

    a =1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b

#print(list(gen_fibon(10)))


def simple_gen():
    for x in range(3):
        yield x

#for num in simple_gen():
    #print(num)

g = simple_gen()

# print(g)#remembers this value and doesnot print it out
#prints the next value and remembers the previous one (yield operation )
print(next(g))
print(next(g))
print(next(g))