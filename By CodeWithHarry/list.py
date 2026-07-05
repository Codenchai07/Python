# list method

# sort()if we want in ascending order

lst = [2, 3, 4, 2, 1, 3]

lst.sort()
print(lst)

#if we want in descending order
lst.sort(reverse=True)
print(lst)

#append()
lst.append(7)
print(lst)

#reverse()
lst.reverse()
print(lst)

#index()
print(lst.index(2))#output is 2 bcz the array is sorted and reversed

#count()
print(lst.count(2))

#copy()
m = lst.copy()
print(m)

#insert()
m.insert(4,2)
print(m)

#extend()
newlst = [10,20,30,10]

m.extend(newlst)
print(m)