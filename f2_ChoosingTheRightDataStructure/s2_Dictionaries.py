#Dictionaries
#Ye bilkul apne traditional dictionary ki tarah hota hai
#jo data ko key value pairs mein store karta hai
dict={1:"Vishwajit",2:"Vijay",3:"Dijay",4:"Vishu","name":"Vishwajit"}
print(dict[2])
print(dict["name"])
print(dict.keys())
print(dict.values())

for i in dict.values():
    print(i)

dictonary={
    1:{"name":"Vishwajit","phone":123344555},
    2:{"name":"Vijay","phone":389429292121},
    3:{"name":"Vishu","phone":3231214234}
}
#Accessing the data
print(dictonary[3])


#Adding data in it
dictonary[4]={"name" :"Aakash","phone":231223131}
dictonary[5]={"name" :"Prakash","phone":231223131}
print(dictonary)


#Updating the data in it
dictonary[4]["name"]="Jhakas"
print(dictonary)


#Deleting 
del dictonary[5]
print(dictonary)
print("-"*20)

for i in dictonary:

    print(dictonary[i])