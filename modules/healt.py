import pygame
class Heart(pygame.sprite.Sprite):
    def __init__(self,pos,direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/" + direction)
        self.rect = self.image.get_rect()
        self.rect.y=pos[1]
        self.rect.x=pos[0]
    