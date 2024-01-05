from math import cos, sin, radians
import pygame
from pygame.locals import QUIT, K_ESCAPE, K_w, K_s, K_a, K_d

class Bullet:
    def __init__(self, x, y, angle, window):
        self.x = x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load("Arrow.png")
        window.blit(self.image, (self.x, self.y))

    def update(self, window):
        self.x += 5 * cos(radians(self.angle))
        self.y += 5 * sin(radians(self.angle))
        window.blit(self.image, (self.x, self.y))

class Game:
    def __init__(self):
        pygame.init()
        self.projectiles = []  # Make projectiles an instance variable
        window_size = (1280, 720)
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Rotating Sprite Movement")
        self.clock = pygame.time.Clock()
        self.sprite_pos = [window_size[0] // 2, window_size[1] // 2, 0]
        self.speed = 5
        self.shoot_frame_count = 0

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    return

            self.handle_mouse_input()
            self.handle_keyboard_input()
            self.update_projectiles()
            self.draw_sprite()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_mouse_input(self):
        mouse_x, _ = pygame.mouse.get_pos()
        self.sprite_pos[2] += (180 / 3.14) * -1 * (radians(mouse_x - self.screen.get_width() // 2))
        pygame.mouse.set_pos((self.screen.get_width() // 2, self.screen.get_height() // 2))

    def handle_keyboard_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.sprite_pos[0] -= self.speed * sin(radians(self.sprite_pos[2]))
            self.sprite_pos[1] -= self.speed * cos(radians(self.sprite_pos[2]))
        if keys[K_s]:
            self.sprite_pos[0] += self.speed * sin(radians(self.sprite_pos[2]))
            self.sprite_pos[1] += self.speed * cos(radians(self.sprite_pos[2]))
        if keys[K_a]:
            self.sprite_pos[0] -= self.speed * cos(radians(self.sprite_pos[2]))
            self.sprite_pos[1] += self.speed * sin(radians(self.sprite_pos[2]))
        if keys[K_d]:
            self.sprite_pos[0] += self.speed * cos(radians(self.sprite_pos[2]))
            self.sprite_pos[1] -= self.speed * sin(radians(self.sprite_pos[2]))

        if pygame.mouse.get_pressed()[0] and self.shoot_frame_count <= 0:
            self.shoot_frame_count = 85
            print("BAM")
            self.projectiles.append(Bullet(*self.sprite_pos, self.screen))

        print(self.projectiles)
        self.shoot_frame_count -= 1

    def update_projectiles(self):
        for projectile in self.projectiles:
            projectile.update(self.screen)

    def draw_sprite(self):
        arrow_image = pygame.image.load("Arrow.png")
        rotated_arrow = pygame.transform.rotate(arrow_image, self.sprite_pos[2])
        rotated_rect = rotated_arrow.get_rect(center=(self.sprite_pos[0], self.sprite_pos[1]))
        self.screen.fill((255, 255, 255))
        self.screen.blit(rotated_arrow, rotated_rect.topleft)

if __name__ == "__main__":
    Game()
