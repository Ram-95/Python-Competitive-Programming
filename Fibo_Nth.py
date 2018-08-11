#fibonacci series first n
n_inp = int(input())
for item in range(n_inp):
    n = int(input())
    f1=1
    f2 = 1
    for i in range(n):
        print(f1, end=' ')
        fibo=f1+f2
        f1=f2
        f2=fibo
    print()
