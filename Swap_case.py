#Swap Case

n = input()
l = list(n)
for i in range(len(l)):
    if l[i].islower():
        l[i] = l[i].upper()
    else:
        l[i] = l[i].lower()

s =''.join(l)
print(s)
        
        
