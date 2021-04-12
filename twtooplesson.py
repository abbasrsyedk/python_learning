# # #OBJECT ORIENTED PROGRAMMING

# # # def hello():
# # #     print("hello")

# # # x=1
# # # print(type(x))

# # # string = "hello"
# # # print(string.upper())

# # class Cluss:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #         print(name.upper())
# #     def get_age(self):
# #         return self.age

# #     def set_age(self,age):
# #         self.age = age

# # a = Cluss("Abbas", 34)
# # a.set_age(20)
# # print(a.get_age())

# # students_namelist

# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# class Course:
#     def __init__(self,name,max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#         self.is_active = False

#     def add_student(self,student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
    
#     def get_average_grade(self):
#         value = 0
#         for  student in self.students:
#             value += student.get_grade()
        
#         return value / len(self.students)

# s1 = Student("Abbas", 19 , 95)
# s2 = Student("Divija",19,98)
# s3 = Student("simba", 2 , 90)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class shit:
#     def __init__(self,name,age,color):
#         super().__init__(name,age)
#         self.color=color
# #i need not write self.name again if i want to initialize the
# #main again instead i can just do this super methods

#class attributes
# class Person:
#     number_of_people = 0

#     def __init__(self,name):
#         self.name = name
#         Person.number_of_people += 1

# p1 = Person("Abbas")
# print(Person.number_of_people)
# p2 = Person("divija")
# print(Person.number_of_people)

#class methods

# class Person:
#     number_of_people = 0
#     GRAVITY = -9.8

#     def __init__(self,name):
#         self.name = name
#         Person.add_person()
#     @classmethod
#     def number_of_people(cls):
#         return cls.number_of_people

#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1

    

# p1 = Person("Abbas")
# print(Person.number_of_people())
# p2 = Person("divija")
# print(Person.number_of_people())

