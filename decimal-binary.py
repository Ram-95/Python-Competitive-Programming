#decimal to binary
def binary(num):
    return format(num ,'b')


n_inp = int(input())
for item in range(0,n_inp):
    n = int(input())
    print(binary(n))
