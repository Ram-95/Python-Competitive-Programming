#Badges - Codeforces

b = int(input())
g = int(input())
n = int(input())

decks = []

for i in range(n+1):
    decks.append((i, n-i))

count = 0

#if 1 means boys are minimum else girls are minimum
flag = 1 if min(b,g) == 1 else 0


for idx in decks:
    if flag == 1:
        if idx[0] <= b and idx[1] <= g:
            #print(idx)
            count += 1
    else:
        if idx[1] <= g and idx[0] <= b:
            #print(idx)
            count += 1

print(count)

        
