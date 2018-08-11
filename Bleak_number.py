#Bleak Number
def count_set_bits(n):
    count = 0
    x = format(n,'b')
    for j in range(len(x)):
        if x[j] == '1':
            count = count + 1
    return count


def bleak(num):
    for i in range(num-32,num):
        if i+count_set_bits(i) == num:
            return 0
        
    return 1

n_inp = int(input())
for item in range(n_inp):
    n = int(input())
    print(bleak(n))
