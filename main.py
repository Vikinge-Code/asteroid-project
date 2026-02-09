import pygame  
from constants import *
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    AstField = AsteroidField()   

    Shot.containers = (shots, updatable, drawable)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        
        screen.fill("black") #fills screen color
        dt= clock.tick(60) / 1000
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen) 
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_sahot")
                    shot.kill()
                    asteroid.split()
                
        #log_event("player_hit")
        #print("Game over!")
        #sys.exit()
        pygame.display.flip() #refreshes the screen
        
        
        
if __name__ == "__main__":
    main()
