#Dice Game between Two Players

from random import randint
import time
import sys
print('Welcome to Dice Game\n---------------------------------------------')
player1 = input('Enter the 1st player name: ')
player2 = input('Enter the 2nd player name: ')
print('{} -> 1st Player \n {} -> 2nd Player'.format(player1, player2))

chance = 0      #this is to choose the next player 0 - first player 1- second player
(tries,tries1) = (0,0)      #tries - 1st player  tries1 - 2nd player
(total, total1) = (0,0)
max_score = 36

while(1):        # Iterate until a player is won
    while(chance == 0):     #1st player chance
        print('\n')
        print('{}(1st Player\'s) Chance.. '.format(player1))
        print('-----------------------------------------------')
        roll = int(input('Roll Dice! Press 1 to roll: '))
        if roll == 1:
            dice = randint(1,6)
            total = total + dice
            tries = tries + 1
            print('{}(1st Player) rolled a {} and total is {}'.format(player1, dice, total))
        else:
            print('Press 1 to roll dice.')
            continue
        chance = 1      #giving chance to 2nd player

        if total >= max_score:
            print('\n\n****** GAME OVER *******\n')
            print('\n{}(Player1) Won the Game in {} tries. Congratulations!!!'.format(player1, tries))
            sys.exit()

    while(chance == 1):     #2nd player chance
        print('\n')
        print('{}(2nd Player\'s) Chance.. '.format(player2))
        print('*************************************************')
        roll = int(input('Roll Dice! Press 1 to roll: '))
        if roll == 1:
            dice = randint(1,6)
            total1 = total1 + dice
            tries1 = tries1 + 1
            print('{}(2nd Player) rolled a {} and total is {}'.format(player2, dice, total1))
        else:
            print('Press 1 to roll dice.')
            continue
        chance = 0      #giving chance to 1st player

        if total1 >= max_score:
            print('\n\n****** GAME OVER *******\n')
            print('\n{}(Player1) Won the Game in {} tries. Congratulations!!!'.format(player2, tries1))
            sys.exit()
    

    
