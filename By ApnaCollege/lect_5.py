# i = 1
# while i <= 5:
#     print(f"hello suraj {i}")
#     i += 1


# practice question
# print numbers from 1 to 100

# i = 1
# while i <=100:
#     print(i)
#     i += 1


# print numbers from 100 to 1
# i = 100
# while i >=1:
#     print(i)
#     i -= 1


# print the multiplication table of a number n.
# n = int(input("enter your number: "))
# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {i*n}")
#     i += 1

# print the elements of the following list using a loop
# lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# l = len(lst)
# i = 0

# while i < l:
#     print(lst[i])
#     i += 1


#search for a number x in this tuple using loop
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter your number to find them: "))
# l = len(num)
# i = 0
# while i < l:
#     if(num[i] == x):
#         print(f"the {x} is exist in tuples")
#     i += 1



#for loop
#practice question
# lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in lst:
#     print(el)

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter your number: "))
# idx = 0
# for el in num:
#     if(el == x):
#         print("found at",idx)
#     idx += 1    
#     # if(x == num[el]):
#     #     print(f"found at index {el}")
    
    
#range(start?,stop?,step?)

# for i in range(0,6,1):
#     print(i)
    
# for el in range(5):
#     print(el)
    
# for n in range(0,5):
#     print(n)

#practice questions
# num = int(input("enter your number: "))

# i = 1
# sum = 0
# while i <=num:
#     sum += i
#     i += 1
    
# print(f"the first n natural's sum is {sum}")

num = int(input("enter your number: "))
fact = 1
for i in range(1,num+1,1):
    fact *= i
    
print(fact)