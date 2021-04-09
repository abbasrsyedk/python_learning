
#Counter
#namedtuple
#most_common 
#defaultdict





from collections import Counter

mylist =[1,1,1,1,2,2,3,3,3,3,3,3]

#print(mylist.count(1))

#print(Counter(mylist))#Counter({3: 6, 1: 4, 2: 2})

#print(Counter('adibibaijfjaiuiouhqaadjkna'))

letters = "aaaaaaabbbbbbbcccccccccc"

c = Counter(letters)

#print(c)

#print(c.most_common())

from collections import defaultdict

d = {'a':10}

#print(d['a'])

d = defaultdict(lambda: 0)

#print(d['wrong key'])

mytuple = (1,2,3)

#print(mytuple[0])

from collections import namedtuple

Dog = namedtuple('Dog',['age', 'breed','name'])

sammy = Dog(age=5, breed='husky', name='sam')

#print(sammy.age)