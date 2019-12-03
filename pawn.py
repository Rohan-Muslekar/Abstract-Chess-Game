import character
class Pawn(character.Character):
    '''Pawn'''

    def __init__(self,own,n):
        self.num = n
        self.moves = ['L','R','F','B']
        self.rsteps = 0
        self.csteps = 0
        super().__init__(own)
    def assRnC(self,aturn,mov):
        if aturn:
            if mov in self.moves:
                if mov == 'L':
                    self.rsteps = 0
                    self.csteps = -1
                elif mov == 'R':
                    self.rsteps = 0
                    self.csteps = 1
                elif mov == 'F':
                    self.rsteps = -1
                    self.csteps = 0
                elif mov == 'B':
                    self.rsteps = 1
                    self.csteps = 0

        else:
            if mov in self.moves:
                if mov == 'R':
                    self.rsteps = 0
                    self.csteps = -1
                elif mov == 'L':
                    self.rsteps = 0
                    self.csteps = 1
                elif mov == 'B':
                    self.rsteps = -1
                    self.csteps = 0
                elif mov == 'F':
                    self.rsteps = 1
                    self.csteps = 0