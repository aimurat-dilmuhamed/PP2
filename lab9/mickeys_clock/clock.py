"""
clock.py — Mickey's Clock drawing logic
Renders the Mickey Mouse image as the clock face,
then draws two rotating glove-style hands on top.
Right hand = minutes | Left hand = seconds
"""

import pygame
import math
import time


class MickeysClock:
    def __init__(self, screen, center, face_image_path):
        self.screen = screen
        self.center = center  # (x, y) — center of clock face

        # Load Mickey face image
        try:
            img = pygame.image.load(face_image_path)
            self.face = pygame.transform.scale(img, (420, 420))
            self.face_loaded = True
        except Exception as e:
            print(f"[Clock] Could not load face image: {e}")
            self.face_loaded = False

        self.font_time  = pygame.font.SysFont("Arial", 56, bold=True)
        self.font_label = pygame.font.SysFont("Arial", 20)

    def _draw_hand(self, angle_deg, length, color, width, glove_radius):
        """Draw a clock hand with a Mickey glove circle at the tip."""
        angle_rad = math.radians(angle_deg - 90)  # 0 = top

        tip_x = self.center[0] + length * math.cos(angle_rad)
        tip_y = self.center[1] + length * math.sin(angle_rad)
        stub_x = self.center[0] - (length * 0.15) * math.cos(angle_rad)
        stub_y = self.center[1] - (length * 0.15) * math.sin(angle_rad)

        # Shadow
        pygame.draw.line(self.screen, (0, 0, 0),
                         (int(stub_x + 3), int(stub_y + 3)),
                         (int(tip_x + 3),  int(tip_y + 3)), width + 2)
        # Hand line
        pygame.draw.line(self.screen, color,
                         (int(stub_x), int(stub_y)),
                         (int(tip_x),  int(tip_y)), width)
        # Glove
        pygame.draw.circle(self.screen, (40, 40, 40),
                           (int(tip_x), int(tip_y)), glove_radius + 2)
        pygame.draw.circle(self.screen, (255, 255, 255),
                           (int(tip_x), int(tip_y)), glove_radius)

    def draw(self):
        now = time.localtime()
        minutes = now.tm_min
        seconds = now.tm_sec

        min_angle = minutes / 60 * 360
        sec_angle = seconds / 60 * 360

        # Draw Mickey face as clock background
        if self.face_loaded:
            face_rect = self.face.get_rect(center=self.center)
            self.screen.blit(self.face, face_rect)
        else:
            pygame.draw.circle(self.screen, (255, 220, 120), self.center, 210)
            pygame.draw.circle(self.screen, (80, 60, 0), self.center, 210, 5)

        # Minute hand (right arm) — dark, longer
        self._draw_hand(min_angle, 155, (30, 30, 30), 8, 18)

        # Second hand (left arm) — red, shorter
        self._draw_hand(sec_angle, 130, (180, 20, 20), 5, 14)

        # Center pin
        pygame.draw.circle(self.screen, (20, 20, 20), self.center, 10)
        pygame.draw.circle(self.screen, (255, 60, 0), self.center, 7)

        # Digital time display
        time_str  = time.strftime("%M:%S", now)
        time_surf = self.font_time.render(time_str, True, (255, 255, 255))
        shadow    = self.font_time.render(time_str, True, (0, 0, 0))
        tx, ty = self.center[0], self.center[1] + 255
        self.screen.blit(shadow, shadow.get_rect(center=(tx + 2, ty + 2)))
        self.screen.blit(time_surf, time_surf.get_rect(center=(tx, ty)))

        lm = self.font_label.render("Right hand = Minutes", True, (200, 200, 200))
        ls = self.font_label.render("Left hand  = Seconds", True, (200, 200, 200))
        self.screen.blit(lm, lm.get_rect(center=(tx, ty + 42)))
        self.screen.blit(ls, ls.get_rect(center=(tx, ty + 65)))