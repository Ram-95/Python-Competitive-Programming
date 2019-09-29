#Optimal Currency Exchange - Codeforces

n = int(input())
d = int(input())
e = int(input())

ans = n

i = 0
while n >= (i*5*e):
    ans = min(ans, (n-i*5*e) % d)
    i += 1

print(ans)
        

