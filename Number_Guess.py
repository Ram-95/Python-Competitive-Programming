#Number guesser
from random import randint  #to generate random numbers
import sys  #to include exit()
import time #to include sleep()
rand_num = randint(1,10)
#print(rand_num)
count = 0
while(1):
    count = count + 1
    n = int(input('Enter the Number[1-10]: '))
    if(rand_num == n):
        print('You Guessed it Correctly!!!. Number is: {}'.format(n))
        print('You did it in {} chances.'.format(count))
        time.sleep(3)
        choice = input('Do you want to continue ? (y/n):' )

        if choice == 'n' or choice == 'N':
            sys.exit()
        elif choice == 'y' or choice == 'Y':
            count = 0
            rand_num = randint(1,10)
        else:
            print('Enter either n/y. Program Exiting..')
            time.sleep(1.500)
            sys.exit()
            
    elif(n < rand_num):
        print('Too Low! Enter a number greater.')
    else:
        print('Too High! Enter a number Lower.')

