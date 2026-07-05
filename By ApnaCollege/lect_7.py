# file I/O in python

# read operation
# f = open("sample.txt","r")
# data = f.read()
# print(data)
# f.close()


# write and append operation
# f = open("sample.txt","w")#this is completely change the existing data
# f = open("sample.txt","a")#this is only apend the data with existing data

# # f.write("this is a new line and this is going to clean all the exitsting data in file")
# f.write("\nthis is the another new line")
# f.close()

# r+ mode
# f = open("sample.txt","r+")#this is the read and write with overwrite the data at pointer start
# f.write("hello")
# print(f.read())
# f.close()

# w+ mode
# f = open("sample.txt","w+")#this is the read and write with truncate the entire data
# f.write("hello")
# print(f.read())
# f.close()

# a+ mode
# f = open("sample.txt","a+")#this is the read and write and append the data
# f.write("hello")
# print(f.read())
# f.close()


# with syntax
# with open("sample.txt","r") as f:
#     print(f.read())
#     f.close()

# import os
# os.remove("sample.txt")

# practice question
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


# with open("practice.txt","r") as f:
#     data = f.read()
#     word = "learning"
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("Not found")


#for open file and read the content of the file
# f = open("practice.txt","r")#to open the file
# data = f.read()#read the content of the file
# print(data)#print the content of the file
# f.close()#for close the file


#write operation
# f = open("practice.txt","w")
# f.write("hello everyone i am learning file i/o in python by shradha")
# f.close()

# f = open("practice.txt","a")
# f.write(" this is the append ")
# f.close()

#r+ mode
# f = open("practice.txt","r+")
# f.write("hello suraj")
# data = f.read()
# print(data)


#deleting file
import os
os.remove("pratice.txt")