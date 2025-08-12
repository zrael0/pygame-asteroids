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

    game_start = False
    pause = False
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    big_font = pygame.font.SysFont(None, 50)
    dt = 0

    def clear_screen():
        pygame.Surface.fill(screen, (0,0,0))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        if not game_start:
            clear_screen() 
            if keys[pygame.K_SPACE]:
                game_start = True
            start_text = big_font.render("Press SPACE to start", True, (200,200,200))
            screen.blit(start_text, (480,340))
        if pause:
            clear_screen()
            pause_text = big_font.render("Paused", True, (200,200,200))
            screen.blit(pause_text, (580,340))
            if keys[pygame.K_SPACE]:
                pause = False
        elif game_start:
            clear_screen() 
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
            screen.blit(fps_text, FPS_TEXT)
            dt = clock.tick(60)/1000.0
            if keys[pygame.K_p]:
                pause = True
        pygame.display.flip()

if __name__ == "__main__":
    main()
