import pygame
class Enemy(pygame.sprite.Sprite):

    def __init__(self,animations,direction,action,velx,vely,healt,isAttacking,posX,posY,name, limit):
        pygame.sprite.Sprite.__init__(self)
        self.animations=animations
        self.action=action
        self.actualPositionOfAnimation=0
        self.direction=direction
        self.image = animations[direction][action][0]
        self.rect = self.image.get_rect()
        self.rect.x=posX
        self.rect.y=posY
        self.velx=velx
        self.vely=vely
        self.healt=healt
        self.isAttacking=isAttacking
        self.name=name
        self.limit = limit
        self.counter=0

    def update(self):
        if self.counter%6==0:
            self.counter=0
            self.image = self.animations[self.direction][self.action][self.actualPositionOfAnimation]
            self.actualPositionOfAnimation+=1
            self.actualPositionOfAnimation= self.actualPositionOfAnimation%len(self.animations[self.direction][self.action])

        self.counter+=1
        # print(self.rect,self.limit)
        
        self.rect.x += self.velx
        self.rect.y += self.vely
        # Limit's control

        if self.action == 'Hurt' or self.action == "Attack":
            self.velx = 0
            self.vely = 0

        if self.action != "Idle" and self.action != "Attack" and self.action != "Hurt":
            if self.rect.x <= self.limit[0] and self.direction == 'Left':
                self.direction = 'Down'
                self.vely = 2
                self.velx = 0
            
            elif self.rect.y >= self.limit[2]and self.direction == 'Down':
                self.direction = "Right"
                self.vely = 0
                self.velx = 2
            
            elif self.rect.x >= self.limit[1]and self.direction == 'Right':
                self.direction = 'Up'
                self.velx = 0
                self.vely = -2
            
            elif self.rect.y <= self.limit[3]and self.direction == 'Up':
                self.direction = 'Left'
                self.velx = -2
                self.vely = 0

