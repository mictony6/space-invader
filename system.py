

import pygame
from pygame import rect
pygame.init()


class System:
    def __init__(self, width, height, running=True):
        self.running = running
        self.canvas = pygame.display.set_mode((width, height))
        self.score = 0
        self.font = pygame.freetype.Font('segoe.ttf', 30)

    def fill(self, color):
        self.canvas.fill(color)

    def blit(self, textsurface, location):
        self.canvas.blit(textsurface, location)

    def getKey(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def isRunning(self):
        pygame.display.update()
        return self.running

    def updateScore(self):
        self.score += 1
