# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# We are learning File I/O
# using Java
# I like programming in Java.

# with open("demo.txt", "w") as f:
#     f.write(
#         "Hi everyone \nWe are learning File I/O \nusing Java \nI like programming in Java")
    


#WAF that replace all occurences of "Java" with "python" in above file.
# def writeSentence():
#     with open("demo.txt","r") as f:
#         data = f.read()
    
#     newData = data.replace("Java","python")
#     print(newData)
    
#     with open("demo.txt","w+") as f:
#         f.write(newData)
#     print("--------------------") 
#     if "learning" in newData:
#         print("yes exist")
#     else:
#         print("not yet")
    
# writeSentence()


# def findWord():
#     data = True
#     line_no = 1
#     with open("demo.txt","r") as f:
#         while data:
#             data = f.readline()
#             if "learning" in data:
#                 print(line_no)
#                 return
#             line_no += 1
    
#     return -1
            
# print(findWord())


with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    numbers = []  # collect all numbers here
    num = ""

    for i in range(len(data)):
        if data[i] == ",":
            numbers.append(int(num))  # store instead of just printing
            num = ""
        else:
            num += data[i]

    if num.strip():  # don't forget the last number after the final comma
        numbers.append(int(num.strip()))

    print(numbers)

    total = 0
    for i in numbers:       # iterate over the list, not an int
        if i % 2 == 0:
            total += i

    print(total)