#Concurrent executions
turn = 1
p1 = 0
p2 = 0
while(p1 <= 3 and p2 <= 3):
    while(turn == 1):
        print('Process 1\'s chance!')
        turn = 0
    p1 = p1+1

    while(turn == 0):
        print('Process 0\'s chance!')
        turn = 1
    p2 = p2+1
