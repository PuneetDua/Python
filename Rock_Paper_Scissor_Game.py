# -*- coding: utf-8 -*-
"""

Rock, Paper and Scissor

@author: Puneet Dua

"""

# Reqd for randomly chosing one out of Rock "r", Paper "p", Scissor "s"
import random

want_to_continue = True         # User Input if want to continue the game or not

def RPS_game():
    global want_to_continue
    comp_choice = None

    while want_to_continue:
        comp_choice = random.choice(['r','p','s'])
        user_choice = str(input("Enter your choice... 'r' for rock, 'p' for paper 's' for scissor \n")).lower()
      
        if comp_choice == user_choice:
                result = 'Tie'

        elif (comp_choice == 'r'):
            if (user_choice=='p'):
                result = 'User Won'
            else:
                result = 'Computer Won'

        elif (comp_choice == 'p'):
            if (user_choice=='s'):
                result = 'User Won'
            else:
                result = 'Computer Won'

        elif (comp_choice == 's'):
            if (user_choice=='r'):
                result = 'User Won'
            else:
                result = 'Computer Won'
        
        print('User Chose: ', user_choice)
        print('Computer Chose: ', comp_choice)
        print(result)
        want_to_continue = str(input("Enter Y to continue.. ")).lower()
        want_to_continue = True if want_to_continue=="y" else False
        print(want_to_continue)

if __name__=='__main__':
    RPS_game()

        
        