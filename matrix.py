import re
import pawn
import hero1
import hero2
import hero3
import coordinate
class Matrix:

    def __init__(self,n):
        self.n = n
        self.board = [[None for _ in range(self.n)] for _ in range(self.n)]
        self.__acount = 0
        self.__bcount = 0
    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                char = self.board[i][j]
                if char == None:
                    print('----', end = '    ')
                else:
                    own = char.owned
                    if isinstance(char,pawn.Pawn):
                        kaunsa = 'P'+char.num
                    elif isinstance(char,hero1.Hero1):
                        kaunsa = 'H1'
                    elif isinstance(char,hero2.Hero2):
                        kaunsa = 'H2'
                    print(own + ':' + kaunsa,end = '    ')
            print()
    def assign(self,plist,aturn):
        if aturn:
            for j in range(self.n):
                c = plist[j]
                p = re.compile('P[0-9]')
                if p.match(c):
                    self.board[4][j] = pawn.Pawn('A',c[1])
                elif c == 'H1':
                    self.board[4][j] = hero1.Hero1('A')
                elif c == 'H2':
                    self.board[4][j] = hero2.Hero2('A')
        else:
            for j in range(self.n):
                c = plist[j]
                p = re.compile('P[0-9]')
                if p.match(c):
                    self.board[0][4-j] = pawn.Pawn('B',c[1])
                elif c == 'H1':
                    self.board[0][4-j] = hero1.Hero1('B')
                elif c == 'H2':
                    self.board[0][4-j] = hero2.Hero2('B')
    def currPos(self,aturn,charac):
        if aturn:
            own = 'A'
        else:
            own = 'B'
        
        for i in range(self.n):
            for j in range(self.n):
                ass = self.board[i][j]
                if ass is not None and ass.owned == own:
                    #for pawn
                    if isinstance(ass,pawn.Pawn):
                        if charac[0] == 'P' and charac[1] == ass.num:
                            print("Pawn: {}".format(charac))
                            return (i,j)
                    #for hero1
                    elif isinstance(ass,hero1.Hero1):
                        if charac == 'H1':
                            print("Hero1: {}".format(charac))
                            return (i,j)
                    #for hero2
                    elif isinstance(ass,hero2.Hero2):
                        if charac == 'H2':
                            print("Hero2: {}".format(charac))
                            return (i,j)
                    #for hero3
                    elif isinstance(ass,hero3.Hero3):
                        if charac == 'H3':
                            print("Hero3: {}".format(charac))
                            return (i,j)
        return (None,None)

    def findNextPos(self,aturn,charac,move,cpx,cpy):
        if isinstance(self.board[cpx][cpy],pawn.Pawn):
            p = self.board[cpx][cpy]
            p.assRnC(aturn,move)
            co = coordinate.Coordinate(cpx,cpy)
            co.nextPosXY(p)
            npx , npy = co.npx , co.npy
        elif isinstance(self.board[cpx][cpy],hero1.Hero1):
            h1 = self.board[cpx][cpy]
            h1.assRnC(aturn,move)
            co = coordinate.Coordinate(cpx,cpy)
            co.nextPosXY(h1)
            npx , npy = co.npx , co.npy
        elif isinstance(self.board[cpx][cpy],hero2.Hero2):
            h2 = self.board[cpx][cpy]
            h2.assRnC(aturn,move)
            co = coordinate.Coordinate(cpx,cpy)
            co.nextPosXY(h2)
            npx , npy = co.npx , co.npy
        elif isinstance(self.board[cpx][cpy],hero3.Hero3):
            h3 = self.board[cpx][cpy]
            h3.assRnC(aturn,move)
            co = coordinate.Coordinate(cpx,cpy)
            co.nextPosXY(h3)
            npx , npy = co.npx , co.npy


        return (npx,npy)
    
    def moveAndReplace(self,cpx,cpy,npx,npy):
        charac = self.board[cpx][cpy]

        if not isinstance(charac,hero3.Hero3):
            self.board[cpx][cpy] = None
            self.board[npx][npy] = charac
        else:
            pass
    
    def validCheck(self,aturn,npx,npy):
        charac = self.board[npx][npy]
        #Checking for same character replacements
        if charac is not None:
            if aturn == True and charac.owned == 'A':
                
                return False
            elif aturn == False and charac.owned == 'B':

                return False
        #Checking Out Of Bound Exception
        if npx < 0 or npx >= self.n or npy < 0 or npy >= self.n:

            return False
        return True
        
    
    def checkWinner(self):
        self.__acount = 0
        self.__bcount = 0
        
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] is not None and self.board[i][j].owned == 'A':
                    self.__acount += 1
                elif self.board[i][j] is not None and self.board[i][j].owned == 'B':
                    self.__bcount += 1
        if self.__acount == 0:
            return "B Wins!"
        elif self.__bcount == 0:
            return "A Wins!"
        else:
            return None

