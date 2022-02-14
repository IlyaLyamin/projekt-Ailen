import pygame
import pygame.font
import sys

import all_sprit


def between_bos_lose():
    pygame.init()
    pygame.font.init()

    stars = all_sprit.stars()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")
    stars.draw(screen)
    pygame.mixer.music.stop()

    ino_img = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/инопланетянин_1.png")
    _big_ino_ = pygame.image.load("дизайн/главное окно/инопланетянин.png")
    _next_lvl_ = pygame.image.load("дизайн/game over/next lvl.png")
    _menu_ = pygame.image.load("дизайн/окно выбора скина/menu.png")

    screen.blit(ino_img, (376, 120))

    screen.blit(_big_ino_, (315, 200))

    text_lose = pygame.font.Font("шрифт/shrift.ttf", 45).render("You lose!!!", True, (99, 221, 23))
    screen.blit(text_lose, (315, 20))

    screen.blit(ino_img, (376, 120))
    screen.blit(ino_img, (316, 120))
    screen.blit(ino_img, (436, 120))

    screen.blit(_big_ino_, (313, 200))

    screen.blit(_menu_, (300, 400))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 300 < event.pos[0] < 500 and 400 < event.pos[1] < 500:
                    import menu
                    menu.first_window()
        pygame.display.flip()


between_bos_lose()