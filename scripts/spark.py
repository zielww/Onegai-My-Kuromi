import math
import pygame


class Spark:
    def __init__(self, pos, angle, speed, color=(255, 255, 255)):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed
        self.color = color

    # Convert polar coordinates to cartesian coordinates
    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed

    def render(self, surf, offset=(0, 0)):
        # Create a polygon
        # Lets do a fucking diamond cuz shine bright
        render_points = [
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0],
             self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle + math.pi * 0.5) * self.speed * 0.5 - offset[0],
             self.pos[1] + math.sin(self.angle + math.pi * 0.5) * self.speed * 0.5 - offset[1]),
            (self.pos[0] + math.cos(self.angle + math.pi) * self.speed * 3 - offset[0],
             self.pos[1] + math.sin(self.angle + math.pi) * self.speed * 3 - offset[1]),
            (self.pos[0] + math.cos(self.angle - math.pi * 0.5) * self.speed * 0.5 - offset[0],
             self.pos[1] + math.sin(self.angle - math.pi * 0.5) * self.speed * 0.5 - offset[1]),
        ]

        pygame.draw.polygon(surf, self.color, render_points)
