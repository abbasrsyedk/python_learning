class Circle():

    #class object attribute
    
    pi = 3.14159
    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius*radius*Circle.pi

        #method
    def get_circumference(self):
        return self.radius*Circle.pi*2

mycircle = Circle(30)

print(mycircle.get_circumference())