# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    time_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, )
    player.draw(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)

        # limit the framerate to 60 FPS
        pygame.display.flip()
        dt = time_clock.tick(60) / 1000

if __name__ == "__main__":
    main()

