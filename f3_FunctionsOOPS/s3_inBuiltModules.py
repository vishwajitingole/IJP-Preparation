import math

print(math.pi)
print("-"*40)



import random
print(random.random())
print(random.randint(1,11))
print(random.uniform(1,2))
print("-"*40)

print(random.choice([1,2,3,4,5,6]))

import datetime
print(datetime.datetime.now())
print("-"*40)



from collections import Counter
#It will show many times a data is shown 
list=[1,2,3,4,5,4,4,4,4,4]
print(Counter(list))