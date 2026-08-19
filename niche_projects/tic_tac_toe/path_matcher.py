'''
I need an intellegent bot that can do the work of not letting 
the player win. it's tough though. i need to think out more.
'''


path_ar = [    [' ',' ',' '],
                                [' ',' ',' '],
                                [' ',' ',' ']]

input_row = None
input_colm = None

def match(t):
    choice_row,choice_colm = None,None


    if input_row == 1 and input_colm == 1:
        pass
    elif input_row == 0:
        if input_colm == 0:
            if t[0][2] == 'O': choice_row,choice_colm = 0,1
    
        elif input_colm == 2:
            if t[0][0] == 'O': choice_row,choice_colm = 0
        else: pass
    


#This doesn't work i need better scrap
