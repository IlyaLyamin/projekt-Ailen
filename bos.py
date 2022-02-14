import pygame
import random


class Bos(pygame.sprite.Sprite):

    def __init__(self, screen, lvl):
        super(Bos, self).__init__()
        self.lvl = lvl
        self.screen = screen
        if lvl == 1:
            self.image = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/bos_1_.png")
        if lvl == 2:
            self.image = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/bos_2.png")
        if lvl == 3:
            self.image = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/bos_3.png")

        x = [int(0), int(200), int(400), int(600)]
        y = [int(200), int(400), int(500)]
        self.rect = self.image.get_rect()
        self.rect.x = 700 - random.choice(x)
        self.rect.y = 500 - random.choice(y)

    def draw_bos(self):
        self.screen.blit(self.image, self.rect)