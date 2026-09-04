# This will be my peak until now if I am able to make it

# a terminal py game completly hard coded by me

#necessary files
import os
import sys
import time

# the system to get buffer-less input ( or simultanous input without pressing enter )

if os.name == 'nt':
    #for windows
    import msvcrt
    def get_char():
        return msvcrt.getch().decode('utf-8', errors='ignore')
else:
    #necessary files for the get_char only
    import termios
    import tty

    #main func
    def get_char():
        fd = sys.stdin.fileno() # getting terminal input system ( default 0 )
        old = termios.tcgetattr(fd) # getting a snapshot of terminal before changing input buffer state
        try:
            tty.setcbreak(fd) # main line where the input for terminal is set not storing buffer so no need to press enter
            return sys.stdin.read(1) # reading input
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old) # after input draning the custom 
                                                          # so that terminal doesn't break

#input of size of memory and generating memory
s = int(input("Enter size (Only Odd) : "))

map = [['.' for i in range(s)] for j in range(s)]

#necessary initalizations
pl = int(s/2)
play_state = True
map[pl][pl] = '@'

os.system('clear')

ro = col = pl

while(play_state):

    #display frame
    for i in range(s): 
        for j in range(s):
            print(map[i][j], end=' ')
        print()
    print()
    
    # control + head replacement
    usr = get_char()

    if usr == 'a':
        if (col-1) != -1:
            map[ro][col-1] = '@'
            map[ro][col] = '.'
            col -= 1
        else:
            map[ro][s-1] = '@'
            map[ro][0] = '.'
            col = s-1
    
    elif usr == 'd':
        if (col+1) != s:
            map[ro][col+1] = '@'
            map[ro][col] = '.'
            col+=1
        else:
            map[ro][0] = '@'
            map[ro][s-1] = '.'
            col = 0

    elif usr == 'w':
        if (ro-1) != -1:
            map[ro-1][col] = '@'
            map[ro][col] = '.'
            ro -= 1
        else:
            map[s-1][col] = '@'
            map[0][col] = '.'
            ro = s-1
    
    elif usr == 's':
        if (ro+1) != s:
            map[ro+1][col] = '@'
            map[ro][col] = '.'
            ro+=1
        else:
            map[0][col] = '@'
            map[s-1][col] = '.'
            ro = 0
    
    elif usr == 'q': play_state = False

    # clearing screen and frametime
    time.sleep(0.016)
    os.system('clear')
