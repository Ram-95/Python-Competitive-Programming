#Power of 2 or not
import math
def power_2(num):
    if num & num-1 == 0:
        return 'Yes'
    else:
        return 'No'


n_inp = int(input())
for item in range(0,n_inp):
    n = int(input())
    print(power_2(n))
