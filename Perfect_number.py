#Perfect Number
def perfect(num):
    count = 0
    for i in range(1,num):
        if num%i == 0:
            count = count + i
    if num == count:
        return 1
    else:
        return 0


n_inp = int(input())
for item in range(n_inp):
    n = int(input())
    print(perfect(n))
