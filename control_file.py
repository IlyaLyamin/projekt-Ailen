import pygame
import sys
import random


def control_window():
    # создание окна
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    # прорисовка кнопок и описания

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


control_window()