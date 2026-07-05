# # list and tuples

# # list
# # first way to create a list
# marks = [98.3, 76.3, 67.6, 98.4]
# # print(marks)
# # print(type(marks))

# # second way to create a list
# roll_no = list((3, 4, 5, 6, 6, 3, 6))

# # roll_no.append([1,2,3])
# # print(roll_no)

# # #accessing the elements
# # print(roll_no[2])#positive indexing
# # print(roll_no[-1][-1])#negative indexing

# # slicing the elements
# # print(roll_no[0:3])
# # print(roll_no[::-1])#reverse the list only used by negative indexing

# # append() and extend()
# # roll_no.append(3)
# # print(roll_no)

# # roll_no.extend([3,4,5,3])
# # print(roll_no)

# # insert(), remove() and pop()
# # roll_no.insert(1,40)#insert at given index
# # print(roll_no)
# # roll_no.remove(3)#delete the element by matching them
# # print(roll_no)
# # print(roll_no.pop())#pop delete the element from the last index of list
# # print(roll_no)

# # index() and count()
# # print(roll_no)
# # print(roll_no.index(5))#return the index of given element
# # print(roll_no.count(6))#return the count of same element in list

# # sort(), sorted() and reverse()
# # roll_no.sort()#return the sorted list by accending order
# # print(roll_no)

# # a = sorted(roll_no)#it also return the sorted list but in new list not modifiying the same list
# # print(a)

# # roll_no.reverse()# return the reverse list
# # print(roll_no)

# # test cases
# a = [1, 2, 3]
# # b = a
# # # print(a)
# # # print(b)
# # b.append(4)
# # print(a)
# # print(b)

# # b = a.copy()
# # b.append(4)
# # print(a)
# # print(b)

# # b= [[0]*3]*3
# # b[0][0] = 1
# # print(b)


# # tuples
# t1 = (1, 2, 3, 3, 2, 3, 4, 3)  # this is tuples

# t2 = 4, 5, 6  # this is also a tuples

# # t3 = (4,)# this is also a tuples
# # t = (4)# but this is not a tuples this is included as integer
# # #because comma make it tuples not parentheses
# # print(type(t1))
# # print(type(t2))

# # print(type(t))
# # print(type(t3))

# # accessing the elements from the tuples
# # print(t1[0])#positive indexing
# # print(t1[-1])#negative indexing


# # slicing
# # print(t2[0:2])#positve indexing
# # print(t2[-3:-1])#negative indexing

# # index() and count()

# # print(t1.index(3))#return the first occurence of the given element
# # print(t1.count(3))#return the count of the given element


# # practice questions
# # WAP to ask the user to enter anmes of their 3 favorite movies & store them in a list

# # movies = []

# # mov1 = input("enter your 1st favorite movie name: ")
# # mov2 = input("enter your 2nd favorite movie name: ")
# # mov3 = input("enter your 3rd favorite movie name: ")

# # movies.append(mov1)
# # movies.append(mov2)
# # movies.append(mov3)
# # print(movies)

# # WAP to check if a list contains a palindrome of elements.
# # lst = [1, 2, 3, 4, 1]

# # print(lst)
# # newlst = lst.copy()
# # newlst.reverse()

# # if newlst == lst:
# #     print("palindrome")
# # else:
# #     print("not palindrome")


# # WAP to count the number of students with the "A" grade in the following tuple.
# tup = ("C", "D", "A", "A", "B", "B", "A")

# lst = []
# lst.extend(tup[0:])
# lst.sort()
# print(lst)

# print(lst.count("A"))

import sys
print(sys.version)