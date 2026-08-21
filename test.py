class winner:
    def __init__(self):
        self.lock_state = None

    def winer(self):
        if self.lock_state == 'O' : print('YOU ARE THE WINNEEEER')
        elif self.lock_state == 'X' : print('The bot won....')
        elif self.lock_state == None : print('It was a tie')

w1 = winner()
w1.lock_state = 'O'

print(w1.lock_state)
w1.winer()


