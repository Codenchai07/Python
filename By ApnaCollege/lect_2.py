#String:-
#String is data types that stores a sequence of characters.
#creating string
# a = "suraj"
# b = "kumar"
# c = "thakur"
# finalstr1 = "suraj" + "kumar"
# #Basic operations
# #1.Concatenation
# print(finalstr1)
# print(a+b) 

# finalString = a+b+c
# print(finalString)

# #2.Length of string
# print(len(finalString))
# print(len(finalstr1))
#3.indexing
#s u r a j
#0 1 2 3 4

# str = "peeragarhi"
# ch = str[1]
# print(ch)


#slicing 
str = "suraj kumar"
str2= "SURAJ KUMAR"





#upper and lower method 
# print(str.upper())
# print(str2.lower())



#title() and capitalize()
# print(str.title())
# print(str.capitalize())


str3 = "SuRaJ"
#swapcase()
# print(str3.swapcase())


# #find() and index()

# print(str3.find("a"))

# print(str3.index("a"))

# print(str3.find("z"))

# print(str3.index("z"))

str4 = "papaya"
str5 = "123"
#count()
# print(str4.count("p"))


# print(str4.isalpha())
# print(str5.isdigit())

str6 = " d "
# print(str6.isspace())

# print(str.startswith("s"))
# print(str.endswith("r"))

#replace()

str7 = "i have a car"
# print(str7.replace("car","bmw"))
# print(str.replace("s","k"))

#strip(), lstrip(), rstrip()

# print(str6)
# print(len(str6))
# print(len(str6.strip()))
# print(len(str6.lstrip()))
# print(len(str6.rstrip()))


#split() and join()
s = "a,b,c"
# print(s.split(","))
# print(str7.split())
# print("_".join(s))

#format() and f-strings
# print("Hello {}".format(str))
# print(f"hello {str}")

#encode()
# print(str.encode())
# print("h".encode())

#slicing()
# print(str[1:3])

# name = input("enter your name: ")
# print(len(name))

# n = "ddd$$$$d"
# print(n.count("$"))


#conditional statement
x = 0;
while(x != 0):
    age = int(input("enter your age: "))
    if(age>=18):
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote")
    
