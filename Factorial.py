#Factorial
def factorial(n):
    fact = 1
    if n == 0 or n == 1:
        return fact
    else:
        for i in range(1,n+1):
            fact = fact * i;
        return fact


n_inp = int(input())
for item in range(0,n_inp):
    num = int(input())
    f_str = str(factorial(num))
    first = f_str[0]
    power = len(f_str)-1
    print(first, power)
    
