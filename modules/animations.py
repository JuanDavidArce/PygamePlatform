import pygame

def getSprites(direccion,scale=2.5):
    sprites = []
    n=0
    while True:
        try:
            actualSprite=pygame.image.load(f'{direccion}/{n}.png')
            size = actualSprite.get_size()
            scaleSprite = pygame.transform.scale(actualSprite, (int(size[0]*scale), int(size[1]*scale)))
            sprites.append(scaleSprite)
            n+=1
        except FileNotFoundError:
            return sprites

ANIMATIONS = {
    'Old_Guardian':getSprites('sprites/Old_Guardian'),
    'Magic_Book':getSprites('sprites/Magic_Book'),
    'Knife':getSprites('sprites/Knife'),
    'Beer':getSprites('sprites/Beer'),
    'Water':getSprites('sprites/Water', scale = 1),
    'Principal_Character': {
        'Down': {
            'Attack':getSprites('sprites/Principal_Character/Down/Attack1'), 
            'Death':getSprites('sprites/Principal_Character/Down/Death'),
            'Hurt':getSprites('sprites/Principal_Character/Down/Hurt'),
            'Idle':getSprites('sprites/Principal_Character/Down/Idle'),
            'Walk':getSprites('sprites/Principal_Character/Down/Walk') },

        'Left': {
            'Attack':getSprites('sprites/Principal_Character/Left/Attack1'), 
            'Death':getSprites('sprites/Principal_Character/Left/Death'),
            'Hurt':getSprites('sprites/Principal_Character/Left/Hurt'),
            'Idle':getSprites('sprites/Principal_Character/Left/Idle'),
            'Walk':getSprites('sprites/Principal_Character/Left/Walk') },
        'Right': {
            'Attack':getSprites('sprites/Principal_Character/Right/Attack1'), 
            'Death':getSprites('sprites/Principal_Character/Right/Death'),
            'Hurt':getSprites('sprites/Principal_Character/Right/Hurt'),
            'Idle':getSprites('sprites/Principal_Character/Right/Idle'),
            'Walk':getSprites('sprites/Principal_Character/Right/Walk') },
        'Up': {
            'Attack':getSprites('sprites/Principal_Character/Up/Attack1'), 
            'Death':getSprites('sprites/Principal_Character/Up/Death'),
            'Hurt':getSprites('sprites/Principal_Character/Up/Hurt'),
            'Idle':getSprites('sprites/Principal_Character/Up/Idle'),
            'Walk':getSprites('sprites/Principal_Character/Up/Walk') },

    },
    'Green_Enemy':{
        'Down': {
            'Attack':getSprites('sprites/Green_Enemy/Down/Attack'), 
            'Death':getSprites('sprites/Green_Enemy/Down/Death'),
            'Hurt':getSprites('sprites/Green_Enemy/Down/Hurt'),
            'Idle':getSprites('sprites/Green_Enemy/Down/Idle'),
            'Walk':getSprites('sprites/Green_Enemy/Down/Walk') },
        'Left': {
            'Attack':getSprites('sprites/Green_Enemy/Left/Attack'), 
            'Death':getSprites('sprites/Green_Enemy/Left/Death'),
            'Hurt':getSprites('sprites/Green_Enemy/Left/Hurt'),
            'Idle':getSprites('sprites/Green_Enemy/Left/Idle'),
            'Walk':getSprites('sprites/Green_Enemy/Left/Walk') },
        'Right':  {
            'Attack':getSprites('sprites/Green_Enemy/Right/Attack'), 
            'Death':getSprites('sprites/Green_Enemy/Right/Death'),
            'Hurt':getSprites('sprites/Green_Enemy/Right/Hurt'),
            'Idle':getSprites('sprites/Green_Enemy/Right/Idle'),
            'Walk':getSprites('sprites/Green_Enemy/Right/Walk') },
        'Up': {
            'Attack':getSprites('sprites/Green_Enemy/Up/Attack'), 
            'Death':getSprites('sprites/Green_Enemy/Up/Death'),
            'Hurt':getSprites('sprites/Green_Enemy/Up/Hurt'),
            'Idle':getSprites('sprites/Green_Enemy/Up/Idle'),
            'Walk':getSprites('sprites/Green_Enemy/Up/Walk') },

    },
    'Skeleton_Enemy':{
        'Down': {
            'Attack':getSprites('sprites/Skeleton_Enemy/Down/Attack'), 
            'Death':getSprites('sprites/Skeleton_Enemy/Down/Death'),
            'Hurt':getSprites('sprites/Skeleton_Enemy/Down/Hurt'),
            'Idle':getSprites('sprites/Skeleton_Enemy/Down/Idle'),
            'Walk':getSprites('sprites/Skeleton_Enemy/Down/Walk') },
        'Left': {
            'Attack':getSprites('sprites/Skeleton_Enemy/Left/Attack'), 
            'Death':getSprites('sprites/Skeleton_Enemy/Left/Death'),
            'Hurt':getSprites('sprites/Skeleton_Enemy/Left/Hurt'),
            'Idle':getSprites('sprites/Skeleton_Enemy/Left/Idle'),
            'Walk':getSprites('sprites/Skeleton_Enemy/Left/Walk') },
        'Right':  {
            'Attack':getSprites('sprites/Skeleton_Enemy/Right/Attack'), 
            'Death':getSprites('sprites/Skeleton_Enemy/Right/Death'),
            'Hurt':getSprites('sprites/Skeleton_Enemy/Right/Hurt'),
            'Idle':getSprites('sprites/Skeleton_Enemy/Right/Idle'),
            'Walk':getSprites('sprites/Skeleton_Enemy/Right/Walk') },
        'Up': {
            'Attack':getSprites('sprites/Skeleton_Enemy/Up/Attack'), 
            'Death':getSprites('sprites/Skeleton_Enemy/Up/Death'),
            'Hurt':getSprites('sprites/Skeleton_Enemy/Up/Hurt'),
            'Idle':getSprites('sprites/Skeleton_Enemy/Up/Idle'),
            'Walk':getSprites('sprites/Skeleton_Enemy/Up/Walk') },

    },
}



