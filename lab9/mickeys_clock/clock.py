import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)
        self.center = (screen_width // 2, screen_height // 2)
        
        # Automatic Path Detection
        base_dir = os.path.dirname(__file__)
        img_dir = os.path.join(base_dir, "images")

        # 1. Load Background
        self.bg = pygame.image.load(os.path.join(img_dir, "clock.png"))
        self.bg = pygame.transform.scale(self.bg, self.screen_size)
        
        # 2. Load Mickey's body
        self.mickey_body = pygame.image.load(os.path.join(img_dir, "mikkey.png")).convert_alpha()
        # Scale body to fit the clock (adjust 400, 600 if he looks too big/small)
        self.mickey_body = pygame.transform.scale(self.mickey_body, (400, 600)) 
        self.mickey_rect = self.mickey_body.get_rect(center=self.center)
        
        # 3. Load Hands
        self.min_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_right_centered.png")).convert_alpha()
        self.sec_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_left_centered.png")).convert_alpha()

    def render(self, surface):
        # Layer 1: The Face
        surface.blit(self.bg, (0, 0))
        
        # Layer 2: Mickey's Body
        surface.blit(self.mickey_body, self.mickey_rect.topleft)
        
        # Layer 3: The Time Logic
        now = datetime.datetime.now()
        # -6 degrees per unit (negative for clockwise in Pygame)
        min_angle = -(now.minute * 6)
        sec_angle = -(now.second * 6)

        # Rotate Minutes
        rotated_min = pygame.transform.rotate(self.min_hand_orig, min_angle)
        min_rect = rotated_min.get_rect(center=self.center)
        
        # Rotate Seconds
        rotated_sec = pygame.transform.rotate(self.sec_hand_orig, sec_angle)
        sec_rect = rotated_sec.get_rect(center=self.center)

        # Draw Hands on Top
        surface.blit(rotated_min, min_rect.topleft)
        surface.blit(rotated_sec, sec_rect.topleft)