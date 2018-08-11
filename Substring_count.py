#substring
s = input()
x = input()

count = 0

for i in range(len(s)):
    if s[i:i+3] == x:
        count = count + 1
print(count)
