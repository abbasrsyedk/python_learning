def create_cubes(n):
    result = []
    for x in range(n):
        #result.append(x**3)
        yield x**3
    #return result

#for x in 
print(list(create_cubes(5)))
