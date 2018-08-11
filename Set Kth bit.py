#Set Kth bit
def set_kth_bit(num, k):
    x = format(num, 'b')
    bin_n = x[::-1]
    if bin_n[k] == '1':
        return int(x,2)
    else:
        return int(num+2**k)
        


n_inp = int(input())
for item in range(0,n_inp):
    n,pos = input().split(" ")
    n = int(n)
    pos = int(pos)
    print(set_kth_bit(n,pos))
