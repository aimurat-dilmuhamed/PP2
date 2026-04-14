import pygame
import sys
from clock import MickeyClock

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up display (Matching the aspect ratio of your clock image)
    WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey Mouse Clock")
    
    clock_logic = MickeyClock(WIDTH, HEIGHT)
    timer = pygame.time.Clock()

    running = True
    while running:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Drawing
        clock_logic.render(screen)
        
        # 3. Refresh Screen
        pygame.display.flip()
        
        # 4. Cap Frame Rate
        timer.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()