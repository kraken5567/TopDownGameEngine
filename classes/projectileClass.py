from math import cos, sin, radians
import pygame
import random

class Bullet:

    bullet_pos = [0,0, 0]

    speed = 50

    image = pygame.image.load("Small_bullet.png")
    image_rotated = None 

    cycle_counted = 0

    def __init__(self, position_toRep, window):

        self.bullet_pos = [position_toRep[0],position_toRep[1],position_toRep[2]]

        self.image_rotated = pygame.transform.rotate(self.image, position_toRep[2])
        window.blit(self.image_rotated, self.image_rotated.get_rect(center=(self.bullet_pos[0], self.bullet_pos[1])))

    def update(self, window):
        self.bullet_pos[0] -= self.speed *  sin(radians(self.bullet_pos[2]))
        self.bullet_pos[1] -= self.speed *  cos(radians(self.bullet_pos[2]))

        window.blit(self.image_rotated,(self.bullet_pos[0],self.bullet_pos[1]))

        self.cycle_counted += 1

        if self.cycle_counted > 20:
            return -1
        
class Gun:

    # init stuff
    sound_wav = None
    bullet_num = 1
    spread = [-0,0]

    # frames till shot
    shootTime = 20
    current_shootTime = 20

    name = "UNNAMED_GUN"

    projectiles = []

    def __init__(self,sound_wav,bullets,spread,framesForShot):
        self.sound_wav = sound_wav
        self.bullet_num = bullets
        self.spread = spread
        self.current_shootTime = self.shootTime = framesForShot

    def nameGun(self,name):
        self.name = name

    def shoot(self, sprite_pos, screen):

        if self.current_shootTime <= 0:

            for i in range(self.bullet_num):
                    spread = self.spread.copy()
                    angle = random.choice( spread )

                    self.projectiles.append(Bullet([sprite_pos[0],sprite_pos[1],sprite_pos[2] + angle], screen))

                    spread.pop(spread.index(angle))
            
            self.sound_wav.play()

            print(f"{self.name} was shot!")

            self.current_shootTime = self.shootTime

    def update(self, screen):
         
        self.current_shootTime -= 1
         
        for i, bullet in enumerate(self.projectiles):
            returnVar = bullet.update(screen)
