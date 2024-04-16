#Sets
# {} created with this
# mutable - size and elements can be changed
# No duplicates are allowed
# unordered


#Tuples
# () created with this
# Immutable - size and elements cannot be changed
# Duplicates are allowed
# ordered



#Starting with sets
set= {1,2,3,4,5,6}
print(set)
print(type(set))
print("-"*20)


#Adding element
set.add(7)
print(set)
print("-"*20)

#Remove element
set.remove(3)
print(set)
set.pop()
print(set)
print("-"*20)

#Iterating
for i in set:
    print(i)
print("-"*20)

#Checking the value
print(2 in set)
print("-"*20)


#Union and Intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("Union :", set1 | set2)
print("Intersection",set1& set2)
print(set1-set2)
print(set2-set1)
print("-"*20)

#Clearing
set.clear()
print(set)
print("-"*20)




#Starting with tuples
tuple=(1,2,3,4)
print(tuple)
print("-"*20)


#Accessing tuples
print(tuple[0])
print("-"*20)

#Slicing
print(tuple[1:3])
print("-"*20)



