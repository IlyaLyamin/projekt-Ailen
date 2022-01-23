import pygame
import sys
import controls


def first_window():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")
    DISP_FIRST = pygame.display.set_mode((800, 800))
    fon = pygame.image.load("дизайн/главное окно/инопланетянин.png")
    all_sprite = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    while True:
        DISP_FIRST.blit(fon, (300, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


first_window()
