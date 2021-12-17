import pygame
from animations import ANIMATIONS

import constants
from enemy import Enemy
import platforms

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
        self.doNotTouch = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

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

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

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

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        base = []

        for i in range(0,11):
            base.append([platforms.STONE_PLATFORM_LEFT, 0+i*70, constants.SCREEN_HEIGHT - 40])
        
        for i in range(11, 30):
            base.append([platforms.lava, 0+i*68, constants.SCREEN_HEIGHT - 40])

    
        level = [ 
                  [platforms.STONE_PLATFORM_LEFT, 500, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 500],
                  [platforms.STONE_PLATFORM_LEFT, 800, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 870, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 940, 400],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1260, 280],
                ]

        enemys=[
            Enemy(ANIMATIONS['Skeleton_Enemy'],'Left','Walk',-5,0,100,False,1214,175,'Skeleton_Enemy',[1100,1214,175,175]),
            Enemy(ANIMATIONS['Green_Enemy'],'Left','Attack',0,0,100,False,1214,175,'Green_Enemy',[1214,1214,175,175])

            ]
        level = base + level


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
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


