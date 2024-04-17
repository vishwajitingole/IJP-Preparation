import pandas
import numpy

list=[1,2,3,4,5]


print(pandas.Series([list,list,list]))
print([list,list,list])
print("*"*40)

print(pandas.DataFrame([list,list,list],columns=["A","B","C","D","E"] )) 