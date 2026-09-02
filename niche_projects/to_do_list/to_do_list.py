import json
from os import system,name # to handle clearning the screen
from time import sleep # to sleep

#func to clear screen in any environment
def clear_screen():
    system("cls" if name == "nt" else "clear")

# func to print the todo list
def task_viewer():
    with open('memory.json','r') as f:
        data = json.load(f)
    size_ = len(data['tasks'])
    
    if size_ == 0: print("There are no tasks add some!",end="\n")
    else:
        for i in range(size_):
            print(f"<{i+1}> [{data['tasks'][str(i+1)]}] ")
    print()

# func to print the logo
def print_logo():
    print("\n")
    print(r"                             ┏━ ┏━┃  ┏━ ┏━┛    ")
    print(r"                             ┃ ┃┃ ┃  ┏━┃━━┃    ")
    print(r"                             ┛ ┛━━┛  ━━ ━━┛    ")
    print(r"                        ━┏┛┏━┃┏━ ┏━┃  ┃  ┛┏━┛━┏┛")
    print(r"                         ┃ ┃ ┃┃ ┃┃ ┃  ┃  ┃━━┃ ┃ ")
    print(r"                         ┛ ━━┛━━ ━━┛  ━━┛┛━━┛ ┛ ")
    print("\n")

# func to add task 1 by 1
def task_adder(stri):
    with open('memory.json', 'r') as f:
        data = json.load(f)
    size_ = len(data['tasks'])
    data['tasks'][str(size_+1)] = stri

    with open('memory.json', 'w') as f:
        json.dump(data, f)

# func to delete the last task in the todo list
def del_last_task():
    with open('memory.json', 'r') as f:
        data = json.load(f)
    size_ = len(data['tasks'])
    del data['tasks'][str(size_)]

    with open('memory.json','w') as f:
        json.dump(data, f)

# func to delete selected task
def del_task(tn):
    with open('memory.json', 'r') as f:
        data = json.load(f)
    size_ = len(data['tasks'])
    dif_ = (size_ - tn)
    if dif_ == 0: del_last_task()
    else:
        for i in range(dif_):
            data['tasks'][str(tn)] = data['tasks'][str(tn+1)]
            tn+=1

    with open('memory.json','w') as f:
        json.dump(data, f)

# overall func to handle task deleting
def deleter_task():
    with open('memory.json','r') as f:
        data = json.load(f)
    s = str(len(data['tasks']))
    print("",end="\n")
    i = input('Which task have you completed?: ')
    l_i = i.lower()
    if  l_i == "all":
        t=int(s)
        while(t):
            del_last_task()
            t-=1
        pass
    else:
        while(i<"1" or i>s):
            i = input('Which task have you completed?: ')

        del_task(int(i))
        del_last_task()

# yea main func
def main_func():
    run_state = True
    lock_key = False
    lock_keyx = False
    lock_keyy = False
    while(run_state):
        with open('memory.json') as f:
            data = json.load(f)
        nt = len(data['tasks'])
        
        if lock_key : clear_screen()
        if lock_keyy : clear_screen()
        if lock_keyx: clear_screen()
        
        print_logo()
        print('Print Todo list [1]     Add task [2]      Complete task [3/all]    Quit [q]\n')

        if lock_keyy:
            print('There are no tasks left to be completed :(\n')

        if lock_key : 
            print()
            task_viewer()
            print()
            lock_key = False

        if lock_keyx :
            if nt: 
                print()
                task_viewer()
            if nt == 0: lock_keyy = True
            else:
                deleter_task()
                clear_screen()
            lock_keyx = False
        else:
            ans = input("What do you want to do?: ")
            while(len(ans) != 1) or ((ans<"1" or ans>"4") and (ans<"q" or ans > "q")):
                ans = input("What do you want to do?: ")
                    
            if ans == "1":lock_key = True
            elif ans == "2":
                task = input(f"\n Task no #{nt+1} :  ")
                task_adder(task)
                clear_screen()
            elif ans == "3": lock_keyx = True
            elif ans == "q": 
                run_state = False
                print()
                print("Come by again <3")
                print()
                sleep(3)
                clear_screen()

# yay program running
clear_screen()
main_func()