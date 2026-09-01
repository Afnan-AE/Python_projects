import json
import os
import time

def task_viewer():
    with open('memory.json','r') as f:
        data = json.load(f)
    size_ = len(data['tasks'])
    
    if size_ == 0: print("There are no tasks add some!\n")
    else:
        for i in range(size_):
            print(f"{i+1}# {data['tasks'][str(i+1)]}")
    
def print_logo():
    print("\n")
    print(r"                             ┏━ ┏━┃  ┏━ ┏━┛    ")
    print(r"                             ┃ ┃┃ ┃  ┏━┃━━┃    ")
    print(r"                             ┛ ┛━━┛  ━━ ━━┛    ")
    print(r"                        ━┏┛┏━┃┏━ ┏━┃  ┃  ┛┏━┛━┏┛")
    print(r"                         ┃ ┃ ┃┃ ┃┃ ┃  ┃  ┃━━┃ ┃ ")
    print(r"                         ┛ ━━┛━━ ━━┛  ━━┛┛━━┛ ┛ ")
    print("\n")

def task_adder(stri):
    with open('memory.json', 'r') as f:
        data = json.load(f)
    size_ = len(data['tasks'])
    data['tasks'][str(size_+1)] = stri

    with open('memory.json', 'w') as f:
        json.dump(data, f)
    
def del_last_task():
    with open('memory.json', 'r') as f:
        data = json.load(f)
    size_ = len(data['tasks'])
    del data['tasks'][str(size_)]

    with open('memory.json','w') as f:
        json.dump(data, f)

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

def deleter_task():
    i = int(input('\nWhich task have you completed?: '))
    del_task(i)
    del_last_task()


run_state = True
lock_key = False
lock_keyx = False
while(run_state):
    with open('memory.json') as f:
        data = json.load(f)
    nt = len(data['tasks'])
    
    if lock_key : os.system("clear")

    print_logo()
    print('Print Todo list [1]     Add task [2]      Complete task [3]    Quit [q]\n')

    if lock_key : 
        print()
        task_viewer()
        print()
        lock_key = False

    if lock_keyx :
        print()
        task_viewer()
        deleter_task()
        os.system("clear")
        lock_keyx = False
    else:
        ans = input("What do you want to?: ")
        while(len(ans) != 1) or ((ans<"1" or ans>"4") and (ans<"q" or ans > "q")):
            ans = input("What do you want to?: ")
                  
        if ans == "1":lock_key = True
        elif ans == "2":
            task = input(f"\n Task no #{nt+1} :  ")
            task_adder(task)
            os.system("clear")
        elif ans == "3": lock_keyx = True
        elif ans == "q": 
            run_state = False
            print()
            print("Come by again <3")
            print()
            time.sleep(4)
            os.system("clear")
