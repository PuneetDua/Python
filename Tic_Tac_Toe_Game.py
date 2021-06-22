# -*- coding: utf-8 -*-
"""
        Tic Tac Toe Game app
        
        @author: Puneet Dua
"""

'''
    Actions need to be taken care of
    
- board
- Displaying that board
- Alternate Turns, i.e, playing game
- Check for wins, tie
    - check for rows, columns, diagonal

'''

# Reqd for computer to chose positions randomly
import random

# empty board
board_elements = ["-" for _ in range(0,9)]
# to keep track of vacant positions that will be filled
vacant_positions = [i for i in range(0,9)]

current_player = 'User'
game_still_going= True       # It will keep track to stop if we get winner

Winner=None

# To display the board
def board():
     
    print(board_elements[0]+" | "+board_elements[1]+" | "+board_elements[2])
    print(board_elements[3]+" | "+board_elements[4]+" | "+board_elements[5])
    print(board_elements[6]+" | "+board_elements[7]+" | "+board_elements[8])

# To play the game, handle turns, check for winner/tie
def play_game():
    global Winner
    
    board()         # Display board initially

    while game_still_going:
        handle_turn(current_player)     
        flip_player()
        Winner = check_win()
        check_tie()
    
    
    # The game has ended here
    if Winner == 'X' or Winner == 'O':
        print(Winner + " won.")
    elif Winner == None:
        print("It's a Tie")



# Handling the user and computer turns
#def usr_turn():
def handle_turn(player):
    
    # need to check the winner after each entry, and same will be updated and 
    # game will be stopped
    global Winner
    
    if player == 'User':
        position = int(input("Chose a vacant position from 1-to-9... "))
        while position < 1 or position > 9 or (board_elements[position-1]=='X' 
                                        or board_elements[position-1]=='O'):
            position = int(input("Chose a valid position(1 to 9)... "))
            
        position = position - 1
        board_elements[position] = "X"
    
    
    elif player == 'Computer':
        if vacant_positions!=[]:
            position = random.choice(vacant_positions)
            print(f"Computer Choice is...{position+1}")
            board_elements[position] = 'O'
    
    # Because this position is occupied now, hence, this slot isn't available 
    # for further turns
    vacant_positions.remove(position)
    #print(vacant_positions)

    board()



def flip_player():
    global current_player
    
    if current_player == 'User':
        current_player  = 'Computer'
    else:
        current_player = 'User'      



def check_win():
    
    global game_still_going
    
    #Check rows
    row_1 = board_elements[0] == board_elements[1] == board_elements[2] !='-'
    row_2 = board_elements[3] == board_elements[4] == board_elements[5] !='-'
    row_3 = board_elements[6] == board_elements[7] == board_elements[8] !='-'
    
    if (row_1 or row_2 or row_3):
        game_still_going = False
    
    if row_1:
        return board_elements[0]
    elif row_2:
        return board_elements[3]
    elif row_3:
        return board_elements[6]

    
    #Check columns
    Col_1 = board_elements[0] == board_elements[3] == board_elements[6] !='-'
    Col_2 = board_elements[1] == board_elements[4] == board_elements[7] !='-'
    Col_3 = board_elements[2] == board_elements[5] == board_elements[8] !='-'
    
    if (Col_1 or Col_2 or Col_3):
        game_still_going = False
    
    if Col_1:
        return board_elements[0]
    elif Col_2:
        return board_elements[1]
    elif Col_3:
        return board_elements[2]
    

    #Check diagonals    
    Diag_1 = board_elements[0] == board_elements[4] == board_elements[8] !='-'
    Diag_2 = board_elements[2] == board_elements[4] == board_elements[6] !='-'
    
    if (Diag_1 or Diag_2):
        game_still_going = False
    
    if Diag_1 or Diag_2:
        return board_elements[4]
    
    return None



def check_tie():
    
    global game_still_going
    
    if vacant_positions==[]:
        game_still_going = False



if __name__ == "__main__":
    play_game()
