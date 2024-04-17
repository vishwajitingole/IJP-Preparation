
import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("./googleplaystore.csv")
print(data.head())
print("-"*50)


print(data.describe())
print("-"*50)


d=pd.read_csv("./Students_marks.csv")


plt.plot(d["Name"],d["Mathematics"])
plt.title('Marks of Student in Maths')
plt.xlabel("Students Name")
plt.ylabel("Students Marks")
plt.show()