#Kth bit set or not
def k_bit_set(num, k):
    x = format(num, 'b')
    bin_n = x[::-1]
    if bin_n[k] == '1':
        return 'Yes'
    else:
        return 'No'
        
n_inp = int(input())
for item in range(0,n_inp):
    n = int(input())
    pos = int(input())
    print(k_bit_set(n, pos))
    
