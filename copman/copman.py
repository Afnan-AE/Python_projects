# This will be my peak until now if I am able to make it

# a terminal py game completly hard coded by me

import os
import sys

if os.name == 'nt':
    import msvcrt
    def get_char():
        return msvcrt.getch().decode('utf-8', errors='ignore')
else:
    import termios
    import tty
    def get_char():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

map = ['.','.','.','.','.','.','.']
size = len(map)
place = int(size/2)
map[place] = '@'
play_state = True

os.system('clear')
while(play_state):
    for i in range(size) : print(map[i], end=' ')
    print()
    usr = get_char()
    if usr == 'a':
        map[place - 1] = '@'
        map[place] = '.'
        place -= 1
    elif usr == 'd':
        map[place + 1] = '@'
        map[place] = '.'
        place += 1
    elif usr == 'q': break
    os.system('clear')


