#practice 1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self.radius


# c1 = Circle(4)
# print(c1.area())
# print(c1.perimeter())

#practice 2
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary =salary
        
#     def showDetails(self):
#         print(self.role)
#         print(self.dept)
#         print(self.salary)
        
        
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","75000")
# # e1 = Employee("accountant","Finance",60000)
# e1 = Engineer("suraj",24)
# e1.showDetails()

#practice+3
class Order:
    def __init__(self,item, price):
        self.item = item
        self.price = price
        
    def __gt__(self,o2):
        return self.price > o2.price
        

o1 = Order("colgate",500)
o2 = Order("tea",40)
print(o1 > o2)                                                        
        
        
        