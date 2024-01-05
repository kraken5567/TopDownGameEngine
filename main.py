import pygame
from pygame.locals import QUIT, K_ESCAPE

from classes.playerClass import Player
from classes.enemyClass import Enemy

class Game:

    playerList = []
    enemyList = []

    def __init__(self):

        pygame.mouse.set_visible(False)

        # Create a window
        window_size = (1280, 720)
        self.screen = screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Rotating Sprite Movement")

        self.playerList.append(Player(screen,[window_size[0] // 2, window_size[1] // 2, 0]))

        self.enemyList.append(Enemy(screen,self.playerList))

        self.run()


    def run(self):

        # Main game loop
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
                    running = False

            self.screen.fill((0, 0, 0))

            for player in self.playerList:
                player.update(self.screen)

            for enemy in self.enemyList:
                enemy.update(self.screen,self.playerList)

            # Update the display
            pygame.display.flip()

            clock.tick(60)

        # Quit Pygame
        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    Game()