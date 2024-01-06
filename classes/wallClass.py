import pygame

from typing import overload

from classes.playerClass import Player
from classes.enemyClass import Enemy

class Wall:

    color = (255, 255, 255)

    def __init__(self, size_tuple, loc_tuple ):
        (dX,dY) = size_tuple; (x,y) = loc_tuple
        self.rect = pygame.Rect(x, y, dX, dY)

    def Firstdraw(self,screen,color_tuple):
        self.color = color_tuple
        pygame.draw.rect(screen, color_tuple, self.rect)

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def collide(self, other):
        # Get the rect of the rotated image
        current_rect = other.image_rotated.get_rect()

        # Check for collision
        if current_rect.colliderect(self.rect):
            return True
        else:
            return False
    
    def handle_collide(self, object, screen):
        object_rect = object.image_rotated.get_rect()
        object_rect.move_ip(object.last_pos[0], object.last_pos[1])
    
    def update(self, screen, enemys, players):
        self.draw(screen)

        for player in players:

            print(self.collide(player))

            if self.collide(player):

                self.handle_collide(player, screen)

        for enemy in enemys:

            print(self.collide(enemy))

            if self.collide(enemy):

                self.handle_collide(enemy, screen)
