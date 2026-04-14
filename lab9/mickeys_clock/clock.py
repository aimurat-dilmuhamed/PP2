import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)
        self.center = (screen_width // 2, screen_height // 2)
        
        # Load Assets
        self.bg = pygame.image.load("clock.jpg")
        self.bg = pygame.transform.scale(self.bg, self.screen_size)
        
        # Minutes Hand (Right hand)
        self.min_hand_orig = pygame.image.load("hand_right_centered.png").convert_alpha()
        # Seconds Hand (Left hand)
        self.sec_hand_orig = pygame.image.load("hand_left_centered.png").convert_alpha()

    def render(self, surface):
        # 1. Draw Background
        surface.blit(self.bg, (0, 0))
        
        # 2. Get Time
        now = datetime.datetime.now()
        # We subtract from 0 or use negative because Pygame rotates CCW
        # 360 degrees / 60 units = 6 degrees per unit
        min_angle = -(now.minute * 6)
        sec_angle = -(now.second * 6)

        # 3. Rotate Hands
        # Rotate the minute hand
        rotated_min = pygame.transform.rotate(self.min_hand_orig, min_angle)
        min_rect = rotated_min.get_rect(center=self.center)
        
        # Rotate the second hand
        rotated_sec = pygame.transform.rotate(self.sec_hand_orig, sec_angle)
        sec_rect = rotated_sec.get_rect(center=self.center)

        # 4. Blit to surface
        surface.blit(rotated_min, min_rect.topleft)
        surface.blit(rotated_sec, sec_rect.topleft)