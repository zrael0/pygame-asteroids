import pygame
import sys
from constants import * 
from player import *
from asteroid import * 
from asteroidfield import *

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids) 
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collide_with(asteroid):
                    shot.kill()
                    asteroid.split()
        for obj in drawable:
            obj.draw(screen)

        fps = clock.get_fps()
        fps_text = font.render(f"{fps:.2f} FPS", True, (50,255,50)) 
        screen.blit(fps_text, (10,10))

        dt = clock.tick(60)/1000.0
        pygame.display.flip()

if __name__ == "__main__":
    main()
