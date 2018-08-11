def bit_set(num):
    x = format(num, 'b')
    bin_n = x[::-1]
    if num == 0:
        return 0
    else:
        for i in range(len(bin_n)):
            if bin_n[i] == '1':
                return (i+1)


n_inp = int(input())

for item in range(0,n_inp):
    n = int(input())
    print(bit_set(n))



            
    
    
