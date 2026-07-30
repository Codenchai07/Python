# sets and thier method in python

s = {3, 3, 4, 3, }
# print(s)  # the duplicate value is not consider


info = {"suraj", 3, False, 4.3}

# print(info)
# sets are unordered


# for empty set creation

s1 = set()
s2 = {}
# print(type(s1))
# print(type(s2))


# sets methods
set1 = {1, 2, 3, 4}
set2 = {3, 5, 6, 7}


#union() methods combine all items uniquley 
# print(set1.union(set2))


# set2.update(set1)
# print(set1, set2)

#intersection()
set3 = set1.intersection(set2)
# print(set3)

# #intersection_update()
# set4 = set1.intersection_update(s2)
# print(set4)

#isdisjoint() this method return true when the two sets don't have common element
print(set1.isdisjoint(set2))
