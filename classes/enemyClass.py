import pygame


from random import random
from math import cos, sin, atan, atan2, degrees, radians

from classes.playerClass import Player

class Enemy:

    sprite_pos = [0,0, 0]

    image = pygame.image.load("Enemy.png")
    image_rotated = None

    speed = 1

    def __init__(self, screen, players):
        [x_max, y_max] = screen.get_size()
        self.sprite_pos = [x_max*random(),y_max*random(),0]

        self.update(screen, players)

    def update(self, screen, players):

        for player in players:
            if True: # check line of sight here


                if player.sprite_pos[0] > self.sprite_pos[0]:
                    self.sprite_pos[0] += self.speed * sin(self.sprite_pos[2])

                elif player.sprite_pos[0] < self.sprite_pos[0]:
                    self.sprite_pos[0] -= self.speed * sin(self.sprite_pos[2])


                if player.sprite_pos[1] > self.sprite_pos[1]:
                    self.sprite_pos[1] += self.speed * cos(self.sprite_pos[2])

                elif player.sprite_pos[1] < self.sprite_pos[1]:
                    self.sprite_pos[1] -= self.speed * cos(self.sprite_pos[2])

                
                self.sprite_pos[2] = atan2(player.sprite_pos[1] - self.sprite_pos[1] , player.sprite_pos[0] - self.sprite_pos[0])

            print(self.sprite_pos[2])

        self.image_rotated = pygame.transform.rotate(self.image, 0)

        screen.blit(self.image_rotated,(self.sprite_pos[0],self.sprite_pos[1]))