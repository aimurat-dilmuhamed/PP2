"""
Mickey's Clock Application
Right hand = minutes | Left hand = seconds
"""

import pygame
import sys
import os
from clock import MickeysClock

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 750
FPS           = 1
BG_COLOR      = (20, 20, 40)

# Point to the Mickey face image
FACE_IMAGE_PATH = os.path.join("images", "mickey_face.jpeg")


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock_tick = pygame.time.Clock()

    center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
    mickey_clock = MickeysClock(screen, center, FACE_IMAGE_PATH)

    font_title = pygame.font.SysFont("Arial", 36, bold=True)
    font_hint  = pygame.font.SysFont("Arial", 18)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

        screen.fill(BG_COLOR)

        title = font_title.render("Mickey's Clock", True, (255, 220, 0))
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 35)))

        mickey_clock.draw()

        hint = font_hint.render("Press Q to quit", True, (100, 100, 120))
        screen.blit(hint, (10, SCREEN_HEIGHT - 28))

        pygame.display.flip()
        clock_tick.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()