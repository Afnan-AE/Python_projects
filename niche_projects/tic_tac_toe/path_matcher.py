'''
I need an intellegent bot that can do the work of not letting 
the player win. it's tough though. i need to think out more.
'''

from random import randint

class setter:
    def __init__(self):
        self.cr_abs = None
        self.cc_abs = None

    def settnr(self, x, y):
        self.cr_abs = x
        self.cc_abs = y

    def return_value(self):
        return self.cr_abs, self.cc_abs

s1 = setter()

def random_choicer():
    random_row = randint(0,2)
    random_colm = randint(0,2)
    return random_row, random_colm


def path_finder(t, pr, pc):

    cr, cc = None, None
        
    

    # user input is at the middle
    if pr == 1 and pc == 1:
        if t[0][0] == 'O': s1.settnr(2,2)
        elif t[0][1] == 'O': s1.settnr(2,1)
        elif t[0][2] == 'O': s1.settnr(2,0)
        elif t[1][0] == 'O': s1.settnr(1,2)
        elif t[1][2] == 'O': s1.settnr(1,0)
        elif t[2][0] == 'O': s1.settnr(0,2)
        elif t[2][1] == 'O': s1.settnr(0,1)
        elif t[2][2] == 'O': s1.settnr(0,0)

    # user input is at the border
    elif (pr == 0 and pc == 0):
        if t[0][1] == 'O': s1.settnr(0,2)
        elif t[0][2] == 'O': s1.settnr(0,1)
        elif t[2][2] == 'O': s1.settnr(1,1)
        elif t[1][1] == 'O': s1.settnr(2,2)

    elif (pr == 0 and pc == 2):
        if t[0][0] == 'O': s1.settnr(0,1)
        elif t[0][1] == 'O': s1.settnr(0,0)
        elif t[2][0] == 'O': s1.settnr(1,1)
        elif t[1][1] == 'O': s1.settnr(2,0)

    elif (pr == 2 and pc == 0):
        if t[2][1] == 'O': s1.settnr(2,2)
        elif t[2][2] == 'O': s1.settnr(2,1)
        elif t[0][2] == 'O': s1.settnr(1,1)
        elif t[1][1] == 'O': s1.settnr(0,2)
            


    elif (pr == 2 and pc == 2):
        if t[2][1] == 'O': s1.settnr(2,0)
        elif t[2][0] == 'O': s1.settnr(2,1)
        elif t[0][0] == 'O': s1.settnr(1,1)
        elif t[1][1] == 'O': s1.settnr(0,0)

    #user input on the sides

    elif (pr == 0 and pc == 1):
        if t[1][1] == 'O': s1.settnr(2,1)
        elif t[2][1] == 'O': s1.settnr(1,1)

    elif (pr == 2 and pc == 1):
        if t[0][1] == 'O': s1.settnr(1,1)
        elif t[1][1] == 'O': s1.settnr(0,1)
    
    elif (pr == 1 and pc == 0):
        if t[1][2] == 'O': s1.settnr(1,1)
        elif t[1][1] == 'O': s1.settnr(1,2)
    
    elif (pr == 1 and pc == 2):
        if t[1][0] == 'O': s1.settnr(1,1)
        elif t[1][1] == 'O': s1.settnr(1,0)

    
    # gets the co ordinates or not
    cr,cc = s1.return_value()

    # if all fails then basic choice
    if (cr == None and cc == None):
        print('Fail confirmed')
        print(pr, pc)
    #loop for bot to not choose the taken square
        cr,cc = random_choicer()
        if_try = 0
        while(t[cr][cc] != ' '):
            if if_try == 9: break
            cr,cc = random_choicer()
            if_try += 1

    

    return cr, cc
