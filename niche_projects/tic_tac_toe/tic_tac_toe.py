import random
import path_matcher
from os import system

table_3x3 = [[' ',' ',' '],
                              [' ',' ',' '],
                              [' ',' ',' ']]

#asci logo
def print_logo():
    print(r"████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████ ")
    print(r"   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      ")
    print(r"   ██    ██ ██             ██    ███████ ██             ██    ██    ██ █████   ")
    print(r"   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      ")
    print(r"   ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████ ")
    pass

#function to print the table in each try instance
def print_table(table):
    print("",end='\n\n')
    for i in range(3):
        for j in range(3):
            if j == 2 : print(f" {table_3x3[i][j]}")
            else : print(f" {table_3x3[i][j]} ", end='|')
        if i != 2 : print("-----------",end= '\n')
    print("",end='\n\n')


# for checking empty squares

def blank_checker(t):
    blanks = 0
    for i in [0,1,2]:
        for j in [0,1,2]:
            if t[i][j] == ' ': blanks+=1
            else : pass
    
    if blanks > 0 : return True
    else : return False



#the function for row and diagonal matching
def matcher(t):
    
    def sub_matcher(space_is):
        if space_is == ' ' : return True
        else : return False

    if t[0][0] == t[1][1] == t[2][2] : return sub_matcher(t[0][0])
    elif t[0][2] == t[1][1] == t[2][0] : return sub_matcher(t[0][2])
    elif t[0][0] == t[0][1] == t[0][2] : return sub_matcher(t[0][0])
    elif t[1][0] == t[1][1] == t[1][2] : return sub_matcher(t[1][0])
    elif t[2][0] == t[2][1] == t[2][2] : return sub_matcher(t[2][0])
    elif t[0][0] == t[1][0] == t[2][0] : return sub_matcher(t[0][0])
    elif t[0][1] == t[1][1] == t[2][1] : return sub_matcher(t[0][1])
    elif t[0][2] == t[1][2] == t[2][2] : return sub_matcher(t[0][2])
    else : return True

#Main base game

def main_play():
    
    print_logo()
    print_table(table_3x3)

    my_choice = [None, None]
    my_choice[0] = int(input("Enter row: "))
    my_choice[1] = int(input("Enter coloumn: "))
    while(table_3x3[my_choice[0]-1][my_choice[1]-1] != ' '):
        print("THIS SPACE IS TAKEN !! ", end='\n')

        my_choice[0] = int(input("Enter row: "))
        my_choice[1] = int(input("Enter coloumn: "))

    print("",end="\n")

    table_3x3[my_choice[0]-1][my_choice[1]-1] = 'O'

    #BOT FUNC
    if(blank_checker(table_3x3)):
        choice_row_bot, choice_colm_bot = path_matcher.path_finder(table_3x3, (my_choice[0]-1), (my_choice[1]-1))
        table_3x3[choice_row_bot][choice_colm_bot] = 'X'

    system('clear')

    if(matcher(table_3x3) and blank_checker(table_3x3)):
        main_play()


def play_game():
    
    print_logo()
    print("",end='\n\n')
    answer_1 = input("Do you want to start? [y/n]: ")
    answer_1 = answer_1.lower()
    if answer_1 == 'y':
        system('clear')
        main_play()
        print_logo()
        print_table(table_3x3)
    else : print("Have a great day", end='\n')


    


    answer = input("Do you want to play again? [y/n]: ")

    answer = answer.lower()

    if answer == 'y':
        for i in [0,1,2]:
            for j in [0,1,2]: 
                table_3x3[i][j] = ' '
        play_game()

    else : print("Have a great day", end='\n')

play_game()