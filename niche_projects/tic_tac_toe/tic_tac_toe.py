import random

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
while(table_3x3[choice_row_bot][choice_colm_bot] != ' '):
    choice_row_bot,choice_colm_bot = random_choicer()

table_3x3[choice_row_bot][choice_colm_bot] = 'X'


print_table(table_3x3)