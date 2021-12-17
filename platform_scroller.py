
import pygame
from bullet import *
import constants
import levels
from animations import *
from player import Player

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    # level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    bullets = pygame.sprite.Group()

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height*3 
    active_sprite_list.add(player)

    healtIcon=pygame.image.load('heart.png')
    
    #Loop until the user clicks the close button.
    done = False
    gameOver= False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while not done and not gameOver:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.jump()
                if event.key ==pygame.K_k:
                    player.attack()

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < 0:
                    player.stop()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.change_x > 0:
                    player.stop()
                

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)



        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
       

        # # If the player gets to the end of the level, go to the next level
        # current_position = player.rect.x + current_level.world_shift
        # if current_position < current_level.level_limit:
        #     player.rect.x = 120
        #     if current_level_no < len(level_list)-1:
        #         current_level_no += 1
        #         current_level = level_list[current_level_no]
        #         player.level = current_level

        closeEnemies= pygame.sprite.spritecollide(player,current_level.enemy_list, False)
        #Update action of enemies
        for enemy in current_level.enemy_list:
            if enemy not in closeEnemies and enemy.name!='Green_Enemy':
                if enemy.direction =='Left':
                    enemy.velx=-2
                else:
                    enemy.velx=2

                if enemy.action!='Walk':
                    enemy.actualPositionOfAnimation=0
                    enemy.action='Walk'
        #If we are attacking

        for enemy in closeEnemies:
            enemy.action='Attack'
            player.healt-=0.05
            enemy.velx=0
            if player.attacking:
                enemy.healt-=1
            if enemy.healt<=0:
                current_level.enemy_list.remove(enemy)
        
        for enemy in current_level.enemy_list:
            if enemy.name=='Green_Enemy':
                if enemy.actualPositionOfAnimation ==10 or enemy.actualPositionOfAnimation==15:
                    enemy.isAttacking=True
        
                if enemy.isAttacking and enemy.action=='Attack':
                    velxBullet =0
                    velyBullet=0
                    #Right
                    if enemy.direction=="Right":
                        pos=[enemy.rect.x + 50 , enemy.rect.bottom-50]
                        velxBullet=5

                    #Lef
                    if enemy.direction=="Left":
                        pos=[enemy.rect.x  , enemy.rect.bottom-50]
                        velxBullet=-5
                        

                    bullet=Bullet(pos,velxBullet,velyBullet) # WE CAN CONTROL THE DIRECTON WITH THE SECOND PARAMETER
                    bullets.add(bullet)
                    enemy.isAttacking=False

        
        #Check if a bullet shoot me
        bulletsHitting=pygame.sprite.spritecollide(player, bullets, False)
        for bullet in  bulletsHitting:
            player.healt-=1
            bullets.remove(bullet)


        #Check if a bullet is out of screen
        for bullet in bullets.copy():
            if bullet.rect.x>800 or bullet.rect.x<=0 or bullet.rect.y>600 or bullet.rect.y<=0:
                bullets.remove(bullet)      

            
        #If we have died
        if player.healt<=0:
            player.healt=0
            gameOver=True

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        bullets.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        bullets.update()
        screen.blit(healtIcon, [20,560])
        myfont =pygame.font.Font('./Storytime.ttf',25)
        healt=myfont.render(str(int(player.healt)), True , constants.WHITE)
        screen.blit(healt, (50,560))
        pygame.draw.rect(screen, constants.RED, pygame.Rect(20, 550, player.healt, 10))


        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        screen.fill(constants.BLACK)
        Fuente =pygame.font.Font('./Storytime.ttf',30)
        img_texto=Fuente.render('HAS PERDIDO PERROOOOOOOOOOOOOOOOO', True, constants.WHITE)
        screen.blit(img_texto,[200,300])
        pygame.display.flip()
        

     
    pygame.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
