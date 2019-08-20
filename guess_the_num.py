# -*- coding: utf-8 -*-
import random
num_games = input('How many games would you like to play? ')
num_games = int(num_games)

while num_games > 0:
    lucky_num = random.randint(1,26) 
    number = input('Enter a randon number between 1-25 :')
    number = int(number)
    guesses=0
    while number != lucky_num:
        guesses+=1
        if number < lucky_num:
            number=int(input('Your guess is lower. Take another guess :'))
        if number > lucky_num:
            number=int(input('Your guess is higher. Take another guess :'))
        
    if number==lucky_num:
        print('Hurray!! you guessed it right,{} is your lucky number.'.format(number) )        
        

