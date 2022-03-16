a={1,3,4,5,6,7,55,5}
print(a)
print(type(a))
#Empty set creation
b=set()
print(type(b))
b.add(1)
print(b)
#We cannot add list or dict items to set
#But can add tuples to a set
b.add((1,2,3,4,5))
print(b)
