import character
class Hero3(character.Character):
    '''Hero3'''
    def __init__(self,own):
        self.moves = ['FL','FR','BR','BL']
        self.rsteps = 0
        self.csteps = 0
    def assRnC(self,aturn,mov):
        if aturn:
            if mov in self.moves:
                if mov == 'FL':
                    self.rsteps = -2
                    self.csteps = -1
                elif mov == 'FR':
                    self.rsteps = -2
                    self.csteps = 1
                elif mov == 'BL':
                    self.rsteps = 2
                    self.csteps = -1
                elif mov == 'BR':
                    self.rsteps = 2
                    self.csteps = 1
                elif mov == 'LF':
                    self.rsteps = -1
                    self.csteps = -2
                elif mov == 'RF':
                    self.rsteps = -1
                    self.csteps = 2
                elif mov == 'LB':
                    self.rsteps = 1
                    self.csteps = -2
                elif mov == 'RB':
                    self.rsteps = 1
                    self.csteps = 2
                
        else:
            if mov in self.moves:
                if mov == 'BR':
                    self.rsteps = -2
                    self.csteps = -1
                elif mov == 'BL':
                    self.rsteps = -2
                    self.csteps = 1
                elif mov == 'FR':
                    self.rsteps = 2
                    self.csteps = -1
                elif mov == 'FL':
                    self.rsteps = 2
                    self.csteps = 1
                elif mov == 'RB':
                    self.rsteps = -1
                    self.csteps = -2
                elif mov == 'LB':
                    self.rsteps = -1
                    self.csteps = 2
                elif mov == 'RF':
                    self.rsteps = 1
                    self.csteps = -2
                elif mov == 'LF':
                    self.rsteps = 1
                    self.csteps = 2