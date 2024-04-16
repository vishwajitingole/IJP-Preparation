#List 

#We can store different type of data in List
list=[1,"V","@",True]
print(list)

#Accessing the elements through indexing
print(list[2])
print("-"*20)


#We can also modify the list in the this way 
list[1]="Vishwajit"
print(list)
print("-"*20)

#Slicing
#slicing mein kaise first part jo mention kiya hota hai wo atta hai magar last wala part nhi atta
#Slicing ka use karke Python mein list ke hisse ko extract kiya 
#ja sakta hai. list[1:3] ka matlab hai ki slicing index 1 se lekar
# just pehle index 3 tak hai. Matlab ye index 1 aur 2 ke elements ko 
#le lega, lekin index 3 ka element nahi lega. Jaise agar list [10, 20, 30, 40, 50] 
#hai, to list[1:3] [20, 30] dega, kyun ki ye index 1 aur 2 ke elements ko lega, 
#lekin index 3 ka nahi.
print(list[1:3])
print("-"*20)

#Reversing a Strings
print(list[::-1])
print("-"*20)



#append
list2=["Vishwajit","Vikas","Ingole"]
list2.append("Codes")
print(list2)
print("-"*20)


#Remove
list2.remove("Codes")
print(list2)
print("-"*20)


#len
print(len(list2))
print("-"*20)


#Sort
list3=[1,27,1,2,0,10]
print(sorted(list3))
print(list3.index(0))
print(list3.index(27))
print("-"*20)

#Count
print(list3.count(1))
print("-"*20)


#Extend
print(list3)
list3.extend([2,1,0,3,43])
print(list3)
print("-"*20)

#Maximum and Minimum in the list
print(max(list3))
print(min(list3))
print("-"*20)

#Iterating the List
print(list3)

for i in list3:
    print(i)
    
for i in range(len(list3)):
    print(i , list3[i])
    


    
    
#Multidimensional List

multiList=[[1,2,3],[4,5,6],[7,7,8]]
print(multiList)
print(multiList[0])
print(multiList[0][0])
print(multiList[1][1])
print(multiList[2][2])

#Assigning a value
multiList[0][0]=10
print(multiList[0][0])

#Appending a value
multiList.append([1,23,2])
print(multiList)
