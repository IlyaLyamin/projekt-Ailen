import pygame
import sys
import controls
import random


def first_window():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")
    DISP_FIRST = pygame.display.set_mode((800, 800))
    fon = pygame.image.load("дизайн/главное окно/инопланетянин.png")
    all_sprites = pygame.sprite.Group()
    for i in range(150):
        star = pygame.sprite.Sprite(all_sprites)
        star.image = pygame.image.load("дизайн/главное окно/звезда.png")
        star.rect = star.image.get_rect()
        star.rect.x = random.randrange(800)
        star.rect.y = random.randrange(800)
    while True:
        all_sprites.draw(screen)
        DISP_FIRST.blit(fon, (300, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


first_window()
