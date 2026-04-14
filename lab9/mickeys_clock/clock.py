import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen_width, screen_height):
        self.screen_size = (screen_width, screen_height)
        self.center = (screen_width // 2, screen_height // 2)
        
        # 1. Load the background clock face
        self.bg = pygame.image.load("images/clock.jpg")
        self.bg = pygame.transform.scale(self.bg, self.screen_size)
        
        # 2. Load Mickey's body (The missing piece!)
        self.mickey_body = pygame.image.load("images/mikkey.png").convert_alpha()
        # Scale him to fit nicely in the middle
        self.mickey_body = pygame.transform.scale(self.mickey_body, (400, 600)) 
        self.mickey_rect = self.mickey_body.get_rect(center=self.center)
        
        # 3. Load Hands
        self.min_hand_orig = pygame.image.load("images/hand_right_centered.png").convert_alpha()
        self.sec_hand_orig = pygame.image.load("images/hand_left_centered.png").convert_alpha()

    def render(self, surface):
        # Draw Background first
        surface.blit(self.bg, (0, 0))
        
        # Draw Mickey's body next (behind the hands)
        surface.blit(self.mickey_body, self.mickey_rect.topleft)
        
        # Get Time and Rotate Hands
        now = datetime.datetime.now()
        min_angle = -(now.minute * 6)
        sec_angle = -(now.second * 6)

        rotated_min = pygame.transform.rotate(self.min_hand_orig, min_angle)
        min_rect = rotated_min.get_rect(center=self.center)
        
        rotated_sec = pygame.transform.rotate(self.sec_hand_orig, sec_angle)
        sec_rect = rotated_sec.get_rect(center=self.center)

        # Draw hands on top of everything
        surface.blit(rotated_min, min_rect.topleft)
        surface.blit(rotated_sec, sec_rect.topleft)