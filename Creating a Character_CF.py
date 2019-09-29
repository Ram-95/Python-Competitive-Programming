#Creating a Character - Codeforces

def create_character(s,i,e):
    ans = 0
    if s > i + e:
        ans = e + 1
    elif s + e <= i:
        ans = 0
    else:
        s += e
        ans = ((s-i)+1)//2

    return ans
 
 
t = int(input())
while t:
    (s,i,e) = (map(int, input().split()))
    print(create_character(s,i,e))
    t = t - 1
