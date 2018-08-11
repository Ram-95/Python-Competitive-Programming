#Count of set bits
def count_bits(num):
    count = 0
    x = format(num, 'b')
    for i in range(len(x)):
        if x[i]=='1':
            count = count+1

    return count


n_inp = int(input())
for item in range(0,n_inp):
    n = int(input())
    print(count_bits(n))
