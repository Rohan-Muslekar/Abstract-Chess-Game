import re
import matrix

def justDoIt(M,aturn,charac,move):
    #Get current pos
    posx , posy = M.currPos(aturn,charac)
    print("Current: {},{}".format(posx,posy))
    #Calculate Next Pos
    npx , npy = M.findNextPos(aturn,charac,move,posx,posy)
    #Check Move Valid
    valid = M.validCheck(aturn,npx,npy)

    #Move The Character
    if valid:
        #Move
        M.moveAndReplace(posx,posy,npx,npy)
        return True
    else:
        #Dont Move
        return False
        

if __name__ == "__main__":
    print("Enter Size: ",end = '')
    n = int(input())
    M = matrix.Matrix(n)
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
            v = justDoIt(M,aturn,charac,move)
            if v == False:
                while(not v):
                    print("Player A: ")
                    charac , move = map(str,input().split(':'))
                    v = justDoIt(M,aturn,charac,move)
        else:
            print("Player B: ")
            charac, move = map(str,input().split(':'))
            v = justDoIt(M,aturn,charac,move)
            if v == False:
                while(not v):
                    print("Player B: ")
                    charac , move = map(str,input().split(':'))
                    v = justDoIt(M,aturn,charac,move)
        aturn = not aturn
        M.display()
        res = M.checkWinner()

        if res is not None:
            print(res)
            break

        
