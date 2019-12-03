import character
class Hero1(character.Character):
    '''Hero1'''
    def __init__(self,own):
        self.moves = ['L','R','F','B']
        self.rsteps = 0
        self.csteps = 0
        super().__init__(own)
    def assRnC(self,aturn,mov):
        if aturn:
            if mov in self.moves:
                if mov == 'L':
                    self.rsteps = 0
                    self.csteps = -2
                elif mov == 'R':
                    self.rsteps = 0
                    self.csteps = 2
                elif mov == 'F':
                    self.rsteps = -2
                    self.csteps = 0
                elif mov == 'B':
                    self.rsteps = 2
                    self.csteps = 0

        else:
            if mov in self.moves:
                if mov == 'R':
                    self.rsteps = 0
                    self.csteps = -2
                elif mov == 'L':
                    self.rsteps = 0
                    self.csteps = 2
                elif mov == 'B':
                    self.rsteps = -2
                    self.csteps = 0
                elif mov == 'F':
                    self.rsteps = 2
                    self.csteps = 0