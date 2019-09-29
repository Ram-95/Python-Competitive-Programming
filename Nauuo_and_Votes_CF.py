#Nauuo and Votes - Codeforces

xyz = list(map(int, input().rstrip().split()))

up = xyz[0]
down = xyz[1]
tie = xyz[2]


if tie == 0:
    if up > down:
        print('+')
    elif down > up:
        print('-')
    else:
        print('0')

else:
    if up == down and down == tie:
        print('?')
    elif up == down and tie > up:
        print('?')
    elif up > (down + tie):
        print('+')
    elif up == (down + tie):
        print('?')
    elif down > (up + tie):
        print('-')
    elif down == (up + tie):
        print('?')
    elif max(up,down) == up:
        if down + tie < up:
            print('+')
        elif down + tie == up:
            print('?')
        else:
            print('?')
    elif max(up,down) == down:
        if up + tie < down:
            print('-')
        elif up + tie == down:
            print('?')
        else:
            print('?')
    

                
    
