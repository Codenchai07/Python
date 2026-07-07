#recursion
#examples

#factorial using recursion

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


#n to 1

def tenToone(n):
    if n == 0:
        return
    
    print(n)
    tenToone(n - 1)
    
tenToone(10)

#1 to n

def oneToTen(n):
    if n == 0:
        return
    
    oneToTen(n - 1)
    print(n)


oneToTen(10)

#fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 5

for i in range(5):
    print(fibonacci(i),end=", ")