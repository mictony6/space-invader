import pygame
import random
from math import sqrt

pygame.init()


class Player:
    def __init__(self, image, canvas):
        self.x = 368
        self.y = 450
        self.image = pygame.image.load(image).convert_alpha()
        self.canvas = canvas
        self.changeX = 0
        self.changeY = 0
        self.restricted = False

    def clamp(self):
        if self.x > 800 or self.x < 0 or self.y > 600 or self.y < 0:
            self.x = self.x % 800
            self.y = self.y % 600

    def draw_player(self):
        self.canvas.blit(self.image, (self.x, self.y))

    def move(self, seconds):
        self.x += self.changeX*seconds
        self.y += self.changeY*seconds

    def restrict(self):
        self.restricted = True


class Enemy:
    def __init__(self, image, canvas):
        self.x = random.randint(0, 800)
        self.y = random.randint(50, 200)
        self.image = pygame.image.load(image).convert_alpha()
        self.canvas = canvas
        self.changeX = 150
        self.changeY = 0

    def clamp(self):
        if self.x > 800 - 32:
            self.changeY = 50
            self.changeX = -150
        elif self.x < 0:
            self.changeY = 50
            self.changeX = 150

    def draw_enemy(self):
        self.canvas.blit(self.image, (self.x, self.y))

    def move(self, seconds):
        self.x += self.changeX*seconds
        self.y += self.changeY*seconds

    def is_out(self):
        return self.y > 600

    def respawn(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 200)
        self.changeX = -self.changeX


class Bullet:
    def __init__(self, x, y, image, canvas):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.canvas = canvas
        self.changeX = 0
        self.changeY = -1000
        self.state = False

    def draw_bullet(self, x, y):
        self.x = x
        self.y = y
        self.canvas.blit(self.image, (self.x + 16, self.y))

    def move(self, seconds):
        self.x += self.changeX*seconds
        self.y += self.changeY*seconds

    def is_colliding(self, obj):
        x = self.x - obj.x
        y = self.y - obj.y
        distance = sqrt(x * x + y * y)
        return distance < 32


class Ship(Player):
    def __init__(self, image, canvas):
        super().__init__(image, canvas)

    def is_colliding(self, obj):
        x = self.x - obj.x
        y = self.y - obj.y
        distance = sqrt(x * x + y * y)
        return distance < 16
