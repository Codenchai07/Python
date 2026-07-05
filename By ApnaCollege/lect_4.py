# # Dictionary and set in python
# # Dictionary
# dic = {
#     "name": "suraj",
#     "roll": 87,
#     "dept": "AI/ML"
# }

# # accessing the dict. elements
# # print(dic["name"])
# # # print(dic["names"])#getting error
# # print(dic.get("names"))#this .get() gives none if the key is not present in dictionary

# # adding and updating
# # the dictionary is mutable but the key is immutable you can change the value of key but you can't change the name of the key
# dic["city"] = "mumbai"
# # print(dic)
# dic["age"] = 24
# # print(dic)

# # removing the element from dictionary
# # dic.pop("roll")

# # del dic["name"]# the del command is delete the element

# # dic.clear()# clear the all element from the dictionary
# # print(dic)


# # keys(), values(), and items()
# # print(dic.keys())#returns all the key of dictionary
# # print(dic.values())#retuns all the values of dictionary
# # print(dic.items())# returns set of elements of whole dictionary

# # dic.update({"age" : 25})
# # print(dic)

# # set
collection = {1, 2, 3, 3,  4}

print(collection)
# # print(type(collection))

null_set = set()

null_set.add(5)
null_set.add("suraj")
null_set.add(2)
null_set.add(3)
null_set.add(4)
print(null_set)


print(null_set | collection)
print(null_set & collection)
# # null_set.remove(4)
# # print(null_set)
# # null_set.pop()
# # print(null_set)
# # null_set.clear()
# # print(null_set)

# # print(null_set.union(collection))
# # print(null_set.intersection(collection))



# pratice question 1
# dict = {
#     "table": ("a piece of furniture", "list fo facts & figures"),
#     "cat": "a small animal"
# }

# print(dict["table"][0])
# print(dict["table"][1])
# print(dict["cat"])

# practice question 2
# sets = {"python", "java", "c++", "python",
#         "javascript", "java", "python", "java", "c++", "c"}

# print(f'total class is required to teach all the subject uniquely:- {len(sets)}')

#practice question 3
marks = {}
x = int(input("enter ur math marks: "))
marks.update({"math":x})
y = int(input("enter ur chem marks: "))
marks.update({"chem":y})
z = int(input("enter ur phy marks: "))
marks.update({"phy":z})

print(marks)

