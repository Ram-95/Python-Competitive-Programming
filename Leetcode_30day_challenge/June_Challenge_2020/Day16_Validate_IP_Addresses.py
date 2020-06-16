#Validate IP Address - IPv4 and IPv6

def isIPv4(s):
    try:
        return str(int(s)) == s and int(s) in range(0,256) and s[0] != '-'
    except:
        return False

def isIPv6(s):
    if len(s) > 4:
        return Fase
    try:
        return int(s, 16) >= 0 and s[0] != '-'
    except:
        return False
   
        
def solve(s):
    if s.count('.') == 3 and all(isIPv4(x) for x in s.split('.')):
        return 'IPv4'
    if s.count(':') == 7 and all(isIPv6(x) for x in s.split(':')):
        return 'IPv6'
    else:
        return 'Neither'
        
s = input('Enter IPv4 or IPv6: ').strip()
print(solve(s))
