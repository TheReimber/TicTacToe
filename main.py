import os
import time
# Author Robert Imber
num = 0
clear = lambda: os.system("clear")

class NC:
    def __init__(self):
        self.pos = []
        self.i = 0
        self.num = ''
        self.playagain = ''
        self.counter = 9
        self.playerTurn = True

    def cls(self):
        pass

    def load_defaults(self):
        self.pos.clear()
        self.counter = 9
        for self.i in range(0,9,1):
            self.pos.append(self.i)
        return

    def board(self):

        print(self.pos)
        print(self.pos[0]," | ",self.pos[1]," | ",self.pos[2]," ")
        print("---+-----+----")
        print(self.pos[3]," | ",self.pos[4]," | ",self.pos[5]," ")
        print("---+-----+----")
        print(self.pos[6]," | ",self.pos[7]," | ",self.pos[8]," ")
        return

    def player(self,val):
        # Player is X
        val = val
        match val:
            case 0:
                self.pos[0] = 'X'
            case 1:
                self.pos[1] = 'X'
            case 2:
                self.pos[2] = 'X'
            case 3:
                self.pos[3] = 'X'
            case 4:
                self.pos[4] = 'X'
            case 5:
                self.pos[5] = 'X'
            case 6:
                self.pos[6] = 'X'
            case 7:
                self.pos[7] = 'X'
            case 8:
                self.pos[8] = 'X'

    def playerMove(self):
        if self.playerTurn:
            self.num = input("enter pos ")
            if self.num == "x":
                TTT.endgame()
            else:
                self.player(int(self.num))
                self.counter -= 1
                self.playerTurn= False
        else:
            print ("AI's turn")
    def goal_check(self):
        if self.counter > 0:
            if (self.pos[0] == 'X' and self.pos[1] == 'X' and self.pos[2] == 'X') or \
                    (self.pos[3] == 'X' and self.pos[4] == 'X' and self.pos[5] == 'X') or \
                    (self.pos[6] == 'X' and self.pos[7] == 'X' and self.pos[8] == 'X') or \
                    (self.pos[0] == 'X' and self.pos[3] == 'X' and self.pos[6] == 'X') or \
                    (self.pos[1] == 'X' and self.pos[4] == 'X' and self.pos[7] == 'X') or \
                    (self.pos[2] == 'X' and self.pos[5] == 'X' and self.pos[8] == 'X') or \
                    (self.pos[0] == 'X' and self.pos[4] == 'X' and self.pos[8] == 'X') or \
                    (self.pos[2] == 'X' and self.pos[4] == 'X' and self.pos[6] == 'X'):
                clear()
                TTT.board()
                print("Player Wins")
                TTT.again()

            if (self.pos[0] == 'O' and self.pos[1] == 'O' and self.pos[2] == 'O') or \
                    (self.pos[3] == 'O' and self.pos[4] == 'O' and self.pos[5] == 'O') or \
                    (self.pos[6] == 'O' and self.pos[7] == 'O' and self.pos[8] == 'O') or \
                    (self.pos[0] == 'O' and self.pos[3] == 'O' and self.pos[6] == 'O') or \
                    (self.pos[1] == 'O' and self.pos[4] == 'O' and self.pos[7] == 'O') or \
                    (self.pos[2] == 'O' and self.pos[5] == 'O' and self.pos[8] == 'O') or \
                    (self.pos[0] == 'O' and self.pos[4] == 'O' and self.pos[8] == 'O') or \
                    (self.pos[2] == 'O' and self.pos[4] == 'O' and self.pos[6] == 'O'):
                clear()
                TTT.board()
                TTT.again()
                print("Computer Wins")
        else:
            clear()
            TTT.board()
            print("Its a Tie")
            TTT.again()


    def again(self):
        self.playagain = input("Play again y/n ")

        if self.playagain == 'y':
            self.pos.clear()

            TTT.load_defaults()

        elif self.playagain == 'n':
            clear()
            print('Cheerio')
            TTT.endgame()

    def endgame(self):
        # end game
        exit()

    def ai(self):
        time.sleep(5)

# Program Start and Main Loop
TTT = NC()
TTT.load_defaults()
run = True

while run:
    clear()
    print(TTT.counter)
    TTT.board()
    if TTT.playerTurn == True:
        TTT.playerMove()
        TTT.goal_check()
    else:
        print("AI to Move")
        TTT.ai()
        TTT.playerTurn = True
    TTT.goal_check()



