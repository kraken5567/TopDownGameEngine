import pygame

from math import sqrt, degrees

class SightRay:

    ray_Rect = None
    ray_Surface = None
    ray = None

    size = [1,0]

    zero_point = [0,0, 0]

    def hypotenuse(self, object, object_to_see):
        x_sqrd = (object.sprite_pos[0] - object_to_see.sprite_pos[0])**2
        y_sqrd = (object.sprite_pos[1] - object_to_see.sprite_pos[1])**2
        return sqrt(x_sqrd + y_sqrd)

    def __init__(self, object, object_to_see, radian):
        self.zero_point = [object.sprite_pos[0], object.sprite_pos[1], radian]

        length = self.hypotenuse( object, object_to_see )
        
        self.ray_Rect = pygame.Rect( object.sprite_pos[0], object.sprite_pos[1], 1, length)
        self.ray_Surface = pygame.Surface( (self.ray_Rect.width, self.ray_Rect.height) )

        ray_Surface_Got = self.ray_Surface.get_rect()
        ray_Surface_Got.center = self.ray_Rect.center

        self.ray_Surface = pygame.transform.rotate( self.ray_Surface, degrees(radian) )

    def checkSight(self, walls):
        for wall in walls:
            return
            if self.ray.colliderect():
                pass