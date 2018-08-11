#number Sparse
def sparse(num):
    for i in range(len(num)-1):
        if int(num[i]) & int(num[i+1]):
            return 0;
    return 1;
        


n_inp = int(input())
for item in range(n_inp):
    n = int(input())
    n1 = format(n,'b')
    print(sparse(n1))
