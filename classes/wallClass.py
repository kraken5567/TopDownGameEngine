import pygame

from typing import overload

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
        # issue!
        if self.other.colliderect(other.rect):
            return True
        else:
            return False
    
    def handle_collide(self, object, screen):
        object.rect.move_ip(object.last_pos[0], object.last_pos[1])
        object.update(screen)
    
    def update(self, screen, enemys, players):
        self.draw(screen)

        for player in players:
            if self.collide(player):

                self.handle_collide(player, screen)

        for enemy in enemys:
            if self.collide(enemy):

                self.handle_collide(enemy)
