#Common Divisors - Codeforces
import math

def common_divisors(n):
    count = 0
    
        
    for i in range(1,round(math.sqrt(n))+1):
        if i != n//i:
            if n % i == 0:
                count += 2
        else:
            if n%i == 0:
                count += 1
        
        
    return count

    
n = int(input())
arr = list(map(int, input().rstrip().split()))
m = min(arr)
print(common_divisors(m))
