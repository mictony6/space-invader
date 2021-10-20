import pygame
import sys
import os

pygame.init()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class System:
    def __init__(self, width, height, running=True):
        self.running = running
        self.canvas = pygame.display.set_mode((width, height))
        self.score = 0
        self.font = pygame.freetype.Font(resource_path('segoe.ttf'), 30)

    def fill(self, color):
        self.canvas.fill(color)

    def blit(self, textsurface, location):
        self.canvas.blit(textsurface, location)

    def get_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_score(self):
        self.score += 1
