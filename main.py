import pygame
from modules.bullet import *
import modules.constants as constants 
import modules.levels as levels
from modules.animations import *
from modules.player import Player
from modules.finalBoos import *
from modules.book import *
from modules.healt import *

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    pygame.mixer.init()
    soundBack = pygame.mixer.Sound("./sounds/background.wav")
    soundEnd = pygame.mixer.Sound("./sounds/End.wav")
    soundGameOver = pygame.mixer.Sound("./sounds/GameOver.wav")
    soundHitGreen = pygame.mixer.Sound("./sounds/hit_Green.wav")
    soundHitPrincipal = pygame.mixer.Sound("./sounds/hit_Principal.wav")
    soundPickUpBook = pygame.mixer.Sound("./sounds/pickUpBook.wav")
    soundPickUpHealth = pygame.mixer.Sound("./sounds/Health.wav")
    soundBoss = pygame.mixer.Sound("./sounds/boss.wav")



    pygame.mixer.Sound.play(soundBack, -1)

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    # level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    #Bosses Group
    bosses = pygame.sprite.Group()
    bosses.add(FinalBoss(ANIMATIONS['Old_Guardian'],1000,6700,400))

    # Books group
    books =pygame.sprite.Group()
    books.add(Magic_Book((570,445),ANIMATIONS['Magic_Book'],'LLEGA AL FINAL Y ELIMINA EL JEFE DEL MAL'))
    books.add(Magic_Book((6300,500),ANIMATIONS['Magic_Book'],'ELIMINA EL JEFE Y LIBERA EL REINOOO!!!!'))

    #Bullets Group
    bullets = pygame.sprite.Group()

    # Hearts Group
    hearts = pygame.sprite.Group()
    hearts.add(Heart((6200,400), 'potion.png'))

    #Levels Group
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height*3 
    active_sprite_list.add(player)

    healtIcon=pygame.image.load('img/heart.png')
    
    #FInal text
    text =''
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
                if event.key ==pygame.K_k or event.key ==pygame.K_SPACE:
                    pygame.mixer.Sound.play(soundHitPrincipal)
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
            for bullet in bullets:
                bullet.rect.x-=diff
            for boss in bosses:
                boss.rect.x-=diff
            for book in books:
                book.rect.x-=diff
            for potion in hearts:
                potion.rect.x-=diff



        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
            for bullet in bullets:
                bullet.rect.x+=diff
            for boss in bosses:
                boss.rect.x+=diff
            for book in books:
                book.rect.x+=diff
            for potion in hearts:
                potion.rect.x+=diff
       

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
            if enemy.actualPositionOfAnimation == 0 and enemy.counter == 1 and enemy.name == "Skeleton_Enemy":
                pygame.mixer.Sound.play(soundHitPrincipal)
           
            player.healt-=0.08
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
                    if bullet.rect.x<=800 and bullet.rect.x>=0 and bullet.rect.y<=600 and bullet.rect.y>=0:
                        pygame.mixer.Sound.play(soundHitGreen)
                    enemy.isAttacking=False

        
        #Check if a bullet shoot me
        bulletsHitting=pygame.sprite.spritecollide(player, bullets, False)
        for bullet in  bulletsHitting:
            player.healt-=1
            bullets.remove(bullet)

        #Check if we are touching lava
                
        lavaTouching=pygame.sprite.spritecollide(player, current_level.lava_list, False)
        for lava in  lavaTouching:
            player.healt-=100
        
        #check if we touch a potion
        healtTouching=pygame.sprite.spritecollide(player,hearts,True)
        for potion in healtTouching:
            player.healt=100
            pygame.mixer.Sound.play(soundPickUpHealth)
            pygame.mixer.Sound.play(soundBoss, -1)

        
        #Check if a final boss attack the player
        finalBossAttack= pygame.sprite.spritecollide(player,bosses, False)
        for boss in finalBossAttack:
            if player.attacking:
                boss.healt-=1
            if boss.healt<=0:
                bosses.remove(boss)
                gameOver=True
                text='GANASTE!! AHORA EL REINO ESTA LIBRE DEL MAL'
                soundBack.stop()
                soundBoss.stop()
                pygame.mixer.Sound.play(soundEnd)
            player.healt-=0.084


        #Check if a bullet is out of screen
        for bullet in bullets.copy():
            if bullet.rect.x>800 or bullet.rect.x<=0 or bullet.rect.y>600 or bullet.rect.y<=0:
                bullets.remove(bullet)      


        
            
        #If we have died
        if player.healt<=0:
            player.healt=0
            gameOver=True
            text ='PERDISTE, VUELVE A INTENTARLO'
            soundBack.stop()
            soundBoss.stop()
            pygame.mixer.Sound.play(soundGameOver)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        bullets.draw(screen)
        bosses.draw(screen)
        books.draw(screen)
        hearts.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        hearts.update()
        bullets.update()
        bosses.update()
        screen.blit(healtIcon, [20,560])
        books.update()
        myfont =pygame.font.Font('./Storytime.ttf',25)
        healt=myfont.render(str(int(player.healt)), True , constants.WHITE)
        screen.blit(healt, (50,560))
        pygame.draw.rect(screen, constants.RED, pygame.Rect(20, 550, player.healt, 10))
        
        if not gameOver:
            for boss in bosses:
                bossAux=boss
            pygame.draw.rect(screen, constants.RED, pygame.Rect(bossAux.rect.x, bossAux.rect.y, bossAux.healt//10, 10))




        # Check if we are touching a book
        ls_col=pygame.sprite.spritecollide(player, books, False)
        for book in ls_col:
            myfont =pygame.font.Font('./Storytime.ttf',30)
            txt_info=myfont.render(book.description, True , constants.WHITE)
            screen.blit(txt_info, (5,5))
            if book.actualPositionOfAnimation == 0:
                pygame.mixer.Sound.play(soundPickUpBook)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        
        # Check if we touch a book 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        screen.fill(constants.BLACK)
        Fuente =pygame.font.Font('./Storytime.ttf',30)
        img_texto=Fuente.render(text, True, constants.WHITE)
        screen.blit(img_texto,[200,300])
        pygame.display.flip()
        

     
    pygame.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
