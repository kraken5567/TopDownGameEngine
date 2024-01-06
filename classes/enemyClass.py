import pygame

from random import random
from math import cos, sin, atan, atan2, degrees, radians

from classes.lineOfSightClass import SightRay

class Enemy:

    last_pos = [0,0, 0]

    sprite_pos = [0,0, 0]

    image = pygame.image.load("Enemy.png")
    image_rotated = None

    speed = 1

    def __init__(self, screen, players):
        [x_max, y_max] = screen.get_size()
        self.sprite_pos = [x_max*random(),y_max*random(),0]

        self.update(screen, players)

    def update(self, screen, players):
        updated = False

        for player in players:

            dx = player.sprite_pos[0] - self.sprite_pos[0]
            dy = player.sprite_pos[1] - self.sprite_pos[1]
            TEMP_angle = atan2(dy, dx)

            sight_line = SightRay(self, player, TEMP_angle)

            if True: # check line of sight here

                self.sprite_pos[2] = TEMP_angle

                if (not updated):
                    self.last_pos = self.sprite_pos
                    updated = True

                self.sprite_pos[0] += self.speed * cos(self.sprite_pos[2])
                self.sprite_pos[1] += self.speed * sin(self.sprite_pos[2])

                angle_degrees = degrees(self.sprite_pos[2]) - 90 # Subtracting 90 degrees makes the sprite face the player
                self.image_rotated = pygame.transform.rotate(self.image, -angle_degrees) # Negating the angle because Pygame's y-axis is flipped

                screen.blit(self.image_rotated, (self.sprite_pos[0], self.sprite_pos[1]))