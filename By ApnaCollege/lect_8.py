#OOPS in Python
#class
# class Student:
#     name = "Suraj"
#     def __init__(self):
#         print(self)
#         print("adding new students to the database...")
    
#object creation
# s1 = Student() 
# s2 = Student()
# # print(s1.name)
# print(s1)
# print(s2)


#constructor + method + attributes

# class College:
#     college_name = "marwadi university"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def welcome(self):
#         print("welcom to the college", self.name)
    
# s1 = College("suraj",97)
# print(s1.college_name)
# print(s1.name)
# print(s1.marks)
# s1.welcome()

#practice question
#create student class that takes name & marks of 3 Subjects as arguments in constructor.
#Then create a method to print the average of the marks.

# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         print("this is the constructor which takes input student's details via argument")
#         self.name = name
#         self.marks1 = marks1                          
#         self.marks2 = marks2                         
#         self.marks3 = marks3  
        
#     def average(self):
#         sum = self.marks1 + self.marks2 + self.marks3 
#         avg = sum/3
#         print(f"the average of the marks is {avg}")   
                          

# s1 = Student("suraj", 98, 87, 67)
# s1.average()                       


#static method
# class Suraj:
#     def __init__(self, name):
#         print(f"this is the constructor")
#         self.name = name
#         print(f"hello {name}")
#     #static method to bypass to use non-required self parameter
#     @staticmethod   
#     def message():
#         print("Congrats!")
        
        
# s1 = Suraj("suraj")
# s1.message()
        
#Abstraction
#to hide unnecessary things from user and show only main content that is called abstraction
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         if self.acc and self.clutch == True:
#             print("Car has started...")
#         else:
#             print("Troubles in engine")

# s1 = Car()
# s1.start()


#Encapsulation
# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc
    
#     #debit method
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("your total balance after debited is: ",self.balance)
        
#     #credit method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.",amount,"was credited")
#         print("your total balance after credited is",self.balance)
        
# acc1 = Account(10000,12345)
# print(acc1.balance)
# print(acc1.account_no)
# acc1.debit(5000)
# acc1.credit(10000)


