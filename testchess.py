import re
class Matrix:

    def __init__(self,n):
        self.n = n
        self.board = [[None for _ in range(self.n)] for _ in range(self.n)]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                char = self.board[i][j]
                if char == None:
                    print(char, end = '    ')
                else:
                    own = char.owned
                    if isinstance(char,Pawn):
                        kaunsa = 'P'+char.num
                    elif isinstance(char,Hero1):
                        kaunsa = 'H1'
                    elif isinstance(char,Hero2):
                        kaunsa = 'H2'
                    print(own + ':' + kaunsa,end = '    ')
            print()
    def assign(self,plist,aturn):
        if aturn:
            for j in range(self.n):
                c = plist[j]
                p = re.compile('P[0-9]')
                if p.match(c):
                    self.board[4][j] = Pawn('A',c[1])
                elif c == 'H1':
                    self.board[4][j] = Hero1('A')
                elif c == 'H2':
                    self.board[4][j] = Hero2('A')
        else:
            for j in range(self.n):
                c = plist[j]
                p = re.compile('P[0-9]')
                if p.match(c):
                    self.board[0][4-j] = Pawn('B',c[1])
                elif c == 'H1':
                    self.board[0][4-j] = Hero1('B')
                elif c == 'H2':
                    self.board[0][4-j] = Hero2('B')
    def currPos(self,aturn,charac):
        if aturn:
            own = 'A'
        else:
            own = 'B'
        
        for i in range(self.n):
            for j in range(self.n):
                ass = self.board[i][j]
                if ass.owned == own:
                    if charac == 'P' + ass.num:
                        return (i,j)
        return (None,None)

    def findNextPos(self,aturn,charac,move,cpx,cpy):
        if isinstance(self.board[cpx][cpy],Pawn):
            pawn = self.board[cpx][cpy]
            pawn.assRnC()
            co = Coordinate(cpx,cpy)
            co.nextPosXY(pawn)
            npx , npy = co.npx , co.npy
        elif isinstance(self.board[cpx][cpy],Hero1):
            hero1 = self.board[cpx][cpy]
            hero1.assRnC()
            co = Coordinate(cpx,cpy)
            co.nextPosXY(hero1)
            npx , npy = co.npx , co.npy
        elif isinstance(self.board[cpx][cpy],Hero2):
            hero2 = self.board[cpx][cpy]
            hero2.assRnC()
            co = Coordinate(cpx,cpy)
            co.nextPosXY(hero2)
            npx , npy = co.npx , co.npy
        elif isinstance(self.board[cpx][cpy],Hero3):
            hero3 = self.board[cpx][cpy]
            hero3.assRnC()
            co = Coordinate(cpx,cpy)
            co.nextPosXY(hero3)
            npx , npy = co.npx , co.npy

        return (npx,npy)
    
    def moveAndReplace(self,ppx,ppy,npx,npy):
        return
    
    def validCheck(self,aturn,npx,npy):
        return True
    
    def checkWinner(self):
        return None

class Coordinate:
    def __init__(self,cpx,cpy):
        self.cpx = cpx
        self.cpy = cpy
        self.npx = None
        self.npy = None
    def nextPosXY(self,chr):
        self.npx = self.cpx + chr.rsteps
        self.npy = self.cpy + chr.csteps
    
class Character:
    def __init__(self, own):
        self.owned = own

class Pawn(Character):
    '''Pawn'''

    def __init__(self,own,n):
        self.num = n
        self.moves = ['L','R','F','B']
        self.rsteps = 0
        self.csteps = 0
        super().__init__(own)
    def assRnC(self,mov):
        pass

class Hero1(Character):
    '''Hero1'''
    def __init__(self,own):
        self.moves = ['L','R','F','B']
        self.rsteps = 0
        self.csteps = 0
        super().__init__(own)
    def assRnC(self,mov):
        pass

class Hero2(Character):
    '''Hero2'''
    def __init__(self,own):
        self.moves = ['FL','FR','BR','BL']
        self.rsteps = 0
        self.csteps = 0
        super().__init__(own)
    def assRnC(self.mov):
        pass
class Hero3(Character):
    '''Hero3'''
    def __init__(self,own):
        self.moves = ['FL','FR','BR','BL']
        self.rsteps = 0
        self.csteps = 0
    def assRnC(self,mov):
        pass

def justDoIt(M,aturn,charac,move):
    #Get current pos
    posx , posy = M.currPos(aturn,charac)
    #Calculate Next Pos
    npx , npy = M.findNextPos(aturn,charac,move,posx,posy)

    #Check Move Valid
    valid = M.validCheck(aturn,npx,npy)

    #Move The Character
    if valid:
        #Move
        M.moveAndReplace(posx,posy,npx,npy)
    else:
        #Dont Move
        pass

if __name__ == "__main__":
    n = int(input())
    M = Matrix(n)
    print("Player A(Input): ")
    p1 = list(map(str,input().split()))
    M.assign(p1,True)

    print("Player B(Input): ")
    p2 = list(map(str,input().split()))
    M.assign(p1,False)

    M.display()

    aturn = True

    while(1):
        if aturn:
            print("Player A: ")
            charac , move = map(str,input().split(':'))
            justDoIt(M,aturn,charac,move)
        else:
            #
            print("Player B: ")
            charac, move = map(str,input().split(':'))
            justDoIt(M,aturn,charac,move)
        
        res = M.checkWinner()

        if res not None:
            print(res)
            break
        

        