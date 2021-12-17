import pygame
import constants
class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos,velx,vely, cl=constants.WHITE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,5])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]       
        self.vely= vely
        self.velx=velx

    def update(self):
        self.rect.y += self.vely
        self.rect.x += self.velx