import character
class Hero2(character.Character):
    '''Hero2'''
    def __init__(self,own):
        self.moves = ['FL','FR','BR','BL']
        self.rsteps = 0
        self.csteps = 0
        super().__init__(own)
    def assRnC(self,aturn,mov):
        if aturn:
            if mov in self.moves:
                if mov == 'FL':
                    self.rsteps = -2
                    self.csteps = -2
                elif mov == 'FR':
                    self.rsteps = -2
                    self.csteps = 2
                elif mov == 'BL':
                    self.rsteps = 2
                    self.csteps = -2
                elif mov == 'BR':
                    self.rsteps = 2
                    self.csteps = 2
        else:
            if mov in self.moves:
                if mov == 'BR':
                    self.rsteps = -2
                    self.csteps = -2
                elif mov == 'BL':
                    self.rsteps = -2
                    self.csteps = 2
                elif mov == 'FR':
                    self.rsteps = 2
                    self.csteps = -2
                elif mov == 'FL':
                    self.rsteps = 2
                    self.csteps = 2