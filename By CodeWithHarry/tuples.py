#tuples

tuple1 = (1,2,3,3,4,5)
print(tuple1)

#immutable checking 

# tup1 = ()

# tup1[1] = "suraj"
# tup1[2] = "nisha"#this gives error, tuple object does not support item assingment

# print(tup1)


#tuples method
#count()
print(tuple1.count(3))

#index()
print(tuple1.index(3,3,len(tuple1)))

#