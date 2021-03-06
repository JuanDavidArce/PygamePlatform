import pygame
from modules.animations import ANIMATIONS

import modules.constants as constants
from modules.enemy import Enemy
import modules.platforms as platforms

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.lava_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.lava_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(0,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.lava_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for lava in self.lava_list:
            lava.rect.x += shift_x


        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            enemy.limit[0]+=shift_x
            enemy.limit[1]+=shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("img/background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        lava = []
        base = []
        for i in range(0,11):
            base.append([platforms.STONE_PLATFORM_LEFT, 0+i*70, constants.SCREEN_HEIGHT - 40])
        
        for i in range(11, 40):
            lava.append([platforms.lava, 20+i*68, constants.SCREEN_HEIGHT - 40])
        
        for i in range(43, 90):
            lava.append([platforms.lava, 20+i*68, constants.SCREEN_HEIGHT - 40])

        for i in range(37,44):
            base.append([platforms.STONE_PLATFORM_LEFT, 0+i*70, constants.SCREEN_HEIGHT - 40])
        
        for i in range(70,76):
            base.append([platforms.STONE_PLATFORM_LEFT, 0+i*70, 200])

        for i in range(87,100):
            base.append([platforms.STONE_PLATFORM_LEFT, 0+i*70, constants.SCREEN_HEIGHT - 40])
        
        for i in range(10):
            base.append([platforms.STONE_PLATFORM_LEFT,6880, constants.SCREEN_HEIGHT -  i*40 ])
        
        level = [ 
                  [platforms.STONE_PLATFORM_LEFT, 500, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 500],
                  [platforms.STONE_PLATFORM_LEFT, 800, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 870, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 940, 400],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.STONE_PLATFORM_LEFT, 1920, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1990, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 2060, 280],
                  [platforms.STONE_PLATFORM_LEFT, 2240, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 2310, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 2380, 400],
                  [platforms.STONE_PLATFORM_LEFT, 2540, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 2610, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 2680, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 3350, 200],
                  [platforms.STONE_PLATFORM_MIDDLE, 3600, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 4400, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 4400, 400],
                  [platforms.STONE_PLATFORM_LEFT, 5400, 300],
                  [platforms.STONE_PLATFORM_MIDDLE, 5470, 300],
                  [platforms.STONE_PLATFORM_RIGHT, 5540, 300],
                  [platforms.STONE_PLATFORM_LEFT, 5800, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 5870, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 5940, 500],
                ]

        enemys=[
            Enemy(ANIMATIONS['Skeleton_Enemy'],'Left','Walk',-5,0,100,False,950,300,'Skeleton_Enemy',[790,950,300,300]),
            Enemy(ANIMATIONS['Green_Enemy'],'Left','Attack',0,0,100,False,1214,175,'Green_Enemy',[1214,1214,175,175]),
            Enemy(ANIMATIONS['Green_Enemy'],'Left','Attack',0,0,100,False,2055,175,'Green_Enemy',[1214,1214,175,175]),
            Enemy(ANIMATIONS['Skeleton_Enemy'],'Left','Walk',-5,0,100,False,2680,400,'Skeleton_Enemy',[2500,2680,400,400]),
            Enemy(ANIMATIONS['Skeleton_Enemy'],'Left','Walk',-5,0,100,False,5240,100,'Skeleton_Enemy',[4850,5240,100,100]),
            Enemy(ANIMATIONS['Skeleton_Enemy'],'Left','Walk',-5,0,100,False,4855,100,'Skeleton_Enemy',[4850,5240,100,100]),
            Enemy(ANIMATIONS['Green_Enemy'],'Left','Attack',0,0,100,False,5900,400,'Green_Enemy',[1214,5980,175,175]),
            ]

        
        level = base+level

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in lava:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.lava_list.add(block)

        for enemy in enemys:
            self.enemy_list.add(enemy)



        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3000
        block.rect.y = 280
        block.boundary_top = 100
        block.boundary_bottom = 450
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3900
        block.rect.y = 450
        block.boundary_left = 3900
        block.boundary_right = 4200
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 4600
        block.rect.y = 280
        block.boundary_top = 100
        block.boundary_bottom = 450
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)