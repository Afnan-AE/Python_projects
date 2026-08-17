import random
from os import system

table_3x3 = [[' ',' ',' '],
                              [' ',' ',' '],
                              [' ',' ',' ']]


#function to print the table in each try instance
def print_table(table):
    print("",end='\n\n')
    for i in range(3):
        for j in range(3):
            if j == 2 : print(f" {table_3x3[i][j]}")
            else : print(f" {table_3x3[i][j]} ", end='|')
        if i != 2 : print("-----------",end= '\n')
    print("",end='\n\n')


#function for bot to choice
def random_choicer():
    random_row = random.randint(0,2)
    random_colm = random.randint(0,2)
    return random_row, random_colm

#the function for row and diagonal matching
def matcher(t):
    
    def sub_matcher(space):
        if space == ' ' : return True
        else : return False

    if t[0][0] == t[1][1] == t[2][2] : sub_matcher(t[0][0])
    elif t[0][2] == t[1][1] == t[2][0] : sub_matcher(t[0][2])
    elif t[0][0] == t[0][1] == t[0][2] : sub_matcher(t[0][0])
    elif t[1][0] == t[1][1] == t[1][2] : sub_matcher(t[1][0])
    elif t[2][0] == t[2][1] == t[2][2] : sub_matcher(t[2][0])
    elif t[0][0] == t[1][0] == t[2][0] : sub_matcher(t[0][0])
    elif t[0][1] == t[1][1] == t[2][1] : sub_matcher(t[0][1])
    elif t[0][2] == t[1][2] == t[2][2] : sub_matcher(t[0][2])
    else : return True

#Main base game
def main_play():
    
    try_instance = 1

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

    #loop for bot to not choose the taken square
    choice_row_bot,choice_colm_bot = random_choicer()
    if_try = 0
    while(table_3x3[choice_row_bot][choice_colm_bot] != ' '):
        if if_try == 9: break
        choice_row_bot,choice_colm_bot = random_choicer()
        if_try += 1

    table_3x3[choice_row_bot][choice_colm_bot] = 'X'

    system('clear')

    while(matcher(table_3x3) and try_instance!=6):
        main_play()
        t+=1


main_play()
print_table(table_3x3)