class Coordinate:
    def __init__(self,cpx,cpy):
        self.cpx = cpx
        self.cpy = cpy
        self.npx = None
        self.npy = None
    def nextPosXY(self,chr):
        self.npx = self.cpx + chr.rsteps
        self.npy = self.cpy + chr.csteps