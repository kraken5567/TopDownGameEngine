# Non-Custom Libraries
import pygame
from pygame.locals import K_w, K_s, K_a, K_d, K_LSHIFT, K_RSHIFT
from pygame.locals import K_1, K_2, K_3, K_4

from math import cos, sin, radians

# Custom Made
from classes.projectileClass import Gun

class Player:

    sprite_pos = [0,0, 0]

    image = pygame.image.load("Arrow.png")
    image_rotated = None

    speed = 3
    sprintFactor = 1.8

    window_size = (0,0)


    last_pos = [0,0, 0]

    # gun stuff

    guns = []
    currentGun = None
    gunNames = ["pistol","shotgun","chaingun","double tap"]

    shootFrameCount = 0

    def __init__(self, screen, loc):

        self.guns.append(Gun(pygame.mixer.Sound("sounds\\pistol.wav"),1,[0],25))
        self.guns.append(Gun(pygame.mixer.Sound("sounds\\shotgun.wav"),5,[-7,-5,-2,0,2,5,-7],70))
        self.guns.append(Gun(pygame.mixer.Sound("sounds\\pistol.wav"),1,[-1,0,1],12))
        self.guns.append(Gun(pygame.mixer.Sound("sounds\\doubleTap.wav"),2,[-2,-1,0,1,2],30))

        for i, gun in enumerate(self.guns):
            gun.nameGun(self.gunNames[i])

        self.currentGun = self.guns[0]

        self.sprite_pos = [loc[0], loc[1], loc[2]]
        screen.blit(self.image,(loc[0],loc[1]))

        self.window_size = screen.get_size()

    def update(self, screen):

        self.last_pos = self.sprite_pos 

        # Handle mouse movement
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dTheta = (180 / 3.14) * -1 * (radians( mouse_x - self.window_size[0]//2 ))

        if dTheta == 0:
            pass
        else:
            self.sprite_pos[2] += (180 / 3.14) * -1 * (radians( mouse_x - self.window_size[0]//2 ))
            pygame.mouse.set_pos((self.window_size[0]//2,self.window_size[1]//2))

        # Handle keyboard input for movement
        keys = pygame.key.get_pressed()
        if keys[K_LSHIFT] or keys[K_RSHIFT]:
            speed = self.speed * self.sprintFactor
        else:
            speed = self.speed
            

        if keys[K_w]:
            self.sprite_pos[0] -= speed * sin(radians(self.sprite_pos[2]))
            self.sprite_pos[1] -= speed * cos(radians(self.sprite_pos[2]))
        if keys[K_s]:
            self.sprite_pos[0] += speed * sin(radians(self.sprite_pos[2]))
            self.sprite_pos[1] += speed * cos(radians(self.sprite_pos[2]))
        if keys[K_a]:
            self.sprite_pos[0] -= speed * cos(radians(self.sprite_pos[2]))
            self.sprite_pos[1] += speed * sin(radians(self.sprite_pos[2]))
        if keys[K_d]:
            self.sprite_pos[0] += speed * cos(radians(self.sprite_pos[2]))
            self.sprite_pos[1] -= speed * sin(radians(self.sprite_pos[2]))

        if keys[K_1]:
            self.currentGun = self.guns[0]
        if keys[K_2]:
            self.currentGun = self.guns[1]
        if keys[K_3]:
            self.currentGun = self.guns[2]
        if keys[K_4]:
            self.currentGun = self.guns[3]
        
        for gun in self.guns:
            gun.update(screen)

        if pygame.mouse.get_pressed()[0]:
            self.currentGun.shoot(self.sprite_pos,screen)

        self.image_rotated = pygame.transform.rotate(self.image, self.sprite_pos[2])

        screen.blit(self.image_rotated, self.image_rotated.get_rect(center=(self.sprite_pos[0], self.sprite_pos[1])))