#XOR = (a and not b) or (b and not a)

def XOR(x,y):
    x = a[::-1]
    y = b[::-1]
    if len(x) < len(y):
        x = x.ljust(len(y),'0')
    else:
        y = y.ljust(len(x),'0')
        
    for i in range(len(y)):
        if x[i] != y[i]:
            return i+1
            break


n_inp = int(input())
for item in range(0,n_inp):
    a,b = input().split(" ")
    a = int(a)
    b = int(b)
    #print('{} and {} values'.format(a,b))
    a = format(a,'b')
    b = format(b,'b')
    #print('Binary:{} and {} values'.format(a,b))
    print(XOR(a,b))

