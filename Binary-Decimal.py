#Binary to Decimal
def bin_dec(num):
    return int(num, 2)


n_inp = int(input())
for item in range(0,n_inp):
    n = input()
    print(bin_dec(n))
    
