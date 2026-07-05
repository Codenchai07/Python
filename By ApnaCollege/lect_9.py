# delete in python as object or object attributes
# class Student:
#     def __init__(self,name):
#         self.name = name


# s1 = Student("Suraj")
# print(s1.name)
# del s1.name#del keyword is delete object or object attributes
# print(s1.name)


# private attributes & methods
# class Person:
#     #this is a private attribute
#     __name = "suraj"

#     #this is a private method
#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())

# inheritance
# single level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("landrover")
# print(car1.name)
# print(car1.start())


# mulit-level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.name = brand


# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# print(car1.start())


# multiple inheritance
# class A:
#     vara = "welcome to class A"

# class B:
#     varb = "welcome to class B"
# class C(A,B):
#     varc = "welcome to class C"

# c1 = C()
# print(c1.varb)
# print(c1.varc)
# print(c1.vara)

# super method
# -> super method is used to access methods of the parent class.
# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().start()
#         super().__init__(type)


# car1 = ToyotaCar("fortuner","electric")
# print(car1.name,car1.type)

# class method
# class Person:
#     name = "anonymous"

#     # def changeName(self,name):
#     #     self.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("suraj")
# print(p1.name)
# print(Person.name)

# property decorator
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(98,97,99)
# print(stu1.percentage)
# stu1.phy = 86
# print(stu1.percentage)

# polymorphism
# operator overloading

# print(1 + 2)# add the number
# print("suraj" + "kumar")# concatenate
# print([1, 2, 3] + [4, 5, 6])# merge

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1, 3)
# num1.showNumber()
# num2 = Complex(4, 7)
# num2.showNumber()

# num3 = num1 + num2
# print(num3.showNumber())