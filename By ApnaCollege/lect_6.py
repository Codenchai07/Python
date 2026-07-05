# function and recursion


# def sum(a,b):
#     s = a + b
#     return s

# print(sum(5,6))

# practice 1
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# def lenth(lst):
#     count = 0
#     for i in lst:
#         count += 1
#     return count

# print(lenth(lst))


# practice 2
# def printElement(lst):
#     for i in lst:
#         print(i,end=" ")

# printElement(lst)

# practice 3

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact


# print(factorial(5))


#practice 4
# def moneyConvertor(usd):
#     convertedMoney = usd * 83
#     return convertedMoney

# print(moneyConvertor(2))

#practice 5
# n = int(input("enter your number: "))
# def oddEvenMessage(n):
#     if(n % 2 ==0):
#         print("Even")
#     else:
#         print("Odd")

# oddEvenMessage(n)

#recursion
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)
    
# show(5)


# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
    
#     return n * fact(n - 1)

# print(fact(4))

# def sum(n):
#     if(n == 0):
#         return 0
#     return n + sum(n - 1)

# print(sum(5))


# def printElements(lst,idx):
#     if(idx == len(lst)):
#         return
#     print(lst[idx], end=" ")
#     printElements(lst,idx+1)
    
# printElements(lst,0)