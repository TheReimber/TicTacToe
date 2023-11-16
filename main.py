import numpy as np
import os

# Author Robert Imber
num = 0
clear = lambda: os.system("clear")
class NC():
    def __init__(self):
        self.pos = []
        self.i = 0
        self.num = ''

    def cls(self):
        pass


    def load_defaults(self):
        self.pos.clear()
        for self.i in range(0,9,1):
            self.pos.append(self.i)
        return
    def board(self):
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
        self.num = input("enter pos ")
        if self.num == "x":
            run = False
            TTT.endgame()
        else:
            self.player(int(self.num))
    def goal_check(self):
        if (self.pos[0] and self.pos[1] and self.pos[2] == 'X') or \
                (self.pos[3] and self.pos[4] and self.pos[5] == 'X') or \
                (self.pos[6] and self.pos[7] and self.pos[8] == 'X') or \
                (self.pos[0] and self.pos[3] and self.pos[6] == 'X') or \
                (self.pos[1] and self.pos[4] and self.pos[7] == 'X') or \
                (self.pos[2] and self.pos[5] and self.pos[8] == 'X') or \
                (self.pos[0] and self.pos[4] and self.pos[8] == 'X') or \
                (self.pos[2] and self.pos[4] and self.pos[6] == 'X'):
            clear()
            TTT.board()
            print("Player Wins")
            TTT.again()

        if (self.pos[0] and self.pos[1] and self.pos[2] == 'O') or \
                (self.pos[3] and self.pos[4] and self.pos[5] == 'O') or \
                (self.pos[6] and self.pos[7] and self.pos[8] == 'O') or \
                (self.pos[0] and self.pos[3] and self.pos[6] == 'O') or \
                (self.pos[1] and self.pos[4] and self.pos[7] == 'O') or \
                (self.pos[2] and self.pos[5] and self.pos[8] == 'O') or \
                (self.pos[0] and self.pos[4] and self.pos[8] == 'O') or \
                (self.pos[2] and self.pos[4] and self.pos[6] == 'O'):
            clear()
            TTT.board()
            TTT.again()
            print("Computer Wins")


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

        exit()
TTT = NC()
TTT.load_defaults()
run = True

while run:
    clear()
    TTT.board()
    TTT.playerMove()
    TTT.goal_check()



