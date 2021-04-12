#homwork

class Line():

    coor1 = (3,2)
    coor2 = (8,10)

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return  (y2-y1)/(x2-x1)
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
#** used for power

c1 = (2,3)
c2 = (4,5)
li = Line(c1,c2)

print(li.distance())
print(li.slope())