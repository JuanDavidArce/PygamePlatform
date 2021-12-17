import pygame
class FinalBoss(pygame.sprite.Sprite):

    def __init__(self,animations,healt,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.actualPositionOfAnimation=0
        self.image = animations[0]
        self.rect = self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
        self.healt=healt
        self.counter=0

    def update(self):
        if self.counter%6==0:
            self.counter=0
            self.image = self.animations[self.actualPositionOfAnimation]
            self.actualPositionOfAnimation+=1
            self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations)

        self.counter+=1
       
