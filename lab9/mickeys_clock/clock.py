import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)
        self.center = (screen_width // 2, screen_height // 2)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, "images")

        # 1. Load and Scale Background
        self.bg = pygame.image.load(os.path.join(img_dir, "clock.png"))
        self.bg = pygame.transform.scale(self.bg, self.screen_size)
        
        # 2. Load and Scale Mickey (Behind the hands)
        self.mickey_body = pygame.image.load(os.path.join(img_dir, "mikkey.png")).convert_alpha()
        # Adjusted size to fit the clock face better
        self.mickey_body = pygame.transform.scale(self.mickey_body, (350, 450)) 
        self.mickey_rect = self.mickey_body.get_rect(center=self.center)
        
        # 3. Load and REDUCE SIZE of hands
        # Original hands were too big; scaling them to about 40% of the screen height
        self.min_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_right_centered.png")).convert_alpha()
        self.min_hand_orig = pygame.transform.scale(self.min_hand_orig, (450, 450)) # Smaller scale
        
        self.sec_hand_orig = pygame.image.load(os.path.join(img_dir, "hand_left_centered.png")).convert_alpha()
        self.sec_hand_orig = pygame.transform.scale(self.sec_hand_orig, (450, 450)) # Smaller scale

    def render(self, surface):
        surface.blit(self.bg, (0, 0))
        surface.blit(self.mickey_body, self.mickey_rect.topleft)
        
        now = datetime.datetime.now()
        
        # In your images, the hands are pointing UP, so 0 is 12 o'clock.
        # Minutes: 360 degrees / 60 minutes = 6 degrees per minute.
        # We add a small offset if the hands aren't perfectly aligned.
        min_angle = -(now.minute * 6) 
        sec_angle = -(now.second * 6)

        # Rotate and keep center point fixed
        rotated_min = pygame.transform.rotate(self.min_hand_orig, min_angle)
        min_rect = rotated_min.get_rect(center=self.center)
        
        rotated_sec = pygame.transform.rotate(self.sec_hand_orig, sec_angle)
        sec_rect = rotated_sec.get_rect(center=self.center)

        surface.blit(rotated_min, min_rect.topleft)
        surface.blit(rotated_sec, sec_rect.topleft)