#Print Decimal, Octal, Hexadecimal, and Binary rep of integers
n = int(input())

for i in range(1,n+1):
    dec = format(i,'d')
    bi = format(i,'b')
    hx = format(i,'x').upper()
    oc = format(i,'o')
    print('{}\t{}\t{}\t{}'.format(dec,oc,hx,bi))
