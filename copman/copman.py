# This will be my peak until now if I am able to make it

# a terminal py game completly hard coded by me

from os import system


map = ['.','.','.','.','.','.','.']
size = len(map)
plac = int(size/2)

play_state = True
while(play_state):
    for i in range(size) : print(map[i], end='')
    print()
    map[plac] = '@'
    ipt = input()
    if ipt == 'a' :
        map[plac-1] = '@'
        map[plac] = '.'
    elif ipt == 'd':
        map[plac+1] = '@'
        map[plac] = '.'
    else : pass
    system('clear')

#idkkk