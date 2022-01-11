### Project Debugging Coin Toss


import random
import pyinputplus as pyip

guess = ''

while guess not in ('heads', 'tails'):
    
    #Fix 1: assigned pyinputplus to verify input is valid
    guess = pyip.inputChoice(['heads', 'tails'], '\nGuess the coin toss! Enter heads or tails: \n') 
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads

#Fix 2: Assign heads and tails to a 0 and 1
if toss == 1: toss = 'heads'
elif toss == 0: toss = 'tails'
    
if toss == guess:
    print('You got it!')
    
else:
    #Fix 3: assigned pyinputplus here again to verify second input is valid
    guess = pyip.inputChoice(['heads', 'tails'], '\nNope! Guess again! \n')
    
    if toss == guess:
        print('You got it!')

    else:
        print('Nope. You are really bad at this game.')
