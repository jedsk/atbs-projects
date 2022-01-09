### Chapter 7 Project: Strong Password Detection

#>= 8 characters, Upper and lower, and has >= 1 digit

import re

char = re.compile(r'\S{8,}')
lower_case = re.compile(r'[a-z]')
upper_case = re.compile(r'[A-Z]')
digit = re.compile(r'\d')
                   


Pass = False

while Pass == False:
    x = 0
    print('Create your Password: \nMust contain at least 8 characters, a lower case, an upper case, and a digit')
    pwInput = input()
    
    if char.search(pwInput) == None:
        print('* Must be at least 8 characters')
        x += 1
        
    if lower_case.search(pwInput) == None:
        print('* Must contain one lower case')
        x += 1
        
    if upper_case.search(pwInput) == None:
        print('* Must contain an upper case')
        x += 1
        
    if digit.search(pwInput) == None:
        print('* Must contain a digit')
        x += 1
    
    if x == 0:
        print('Password Saved...')
        break
        
    else: 
        print('\n---Please Try Again---\n')
           
   
