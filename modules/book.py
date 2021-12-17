import pygame
class Magic_Book(pygame.sprite.Sprite):
    def __init__(self,pos,animations,description):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.actualPositionOfAnimation=0
        self.image = animations[0]
        self.rect = self.image.get_rect()
        self.rect.y=pos[1]
        self.rect.x=pos[0]
        self.description=description
    def update(self):
        self.image = self.animations[self.actualPositionOfAnimation]
        self.actualPositionOfAnimation+=1
        self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations)
