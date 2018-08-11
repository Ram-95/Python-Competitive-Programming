#Array reshaping
import numpy as np

l = input().split(' ')
l1=[]
for item in l:
    l1.append(int(item))

my_array = np.array(l1)
my_array = my_array.reshape(3,3)

print(my_array)



