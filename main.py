import pygame  
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") #fills screen color 
        pygame.display.flip() #refreshes the screen



if __name__ == "__main__":
    main()
