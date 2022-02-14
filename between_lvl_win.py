import pygame
import pygame.font
import sys

import all_sprit
from stats import Stats


def between_bos_win(num_bos):
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

    if num_bos == 1:
        score = pygame.font.Font("шрифт/shrift.ttf", 45).render("+10 000 xp", True, (99, 221, 23))
        screen.blit(score, (320, 70))

        screen.blit(_next_lvl_, (430, 400))

        screen.blit(_menu_, (180, 400))

        text = pygame.font.Font("шрифт/shrift.ttf", 40).render("You killed first boss!!!", True, (99, 221, 23))
        screen.blit(text, (250, 20))

    elif num_bos == 2:
        score = pygame.font.Font("шрифт/shrift.ttf", 45).render("+50 000 xp", True, (99, 221, 23))
        screen.blit(score, (320, 70))

        screen.blit(_next_lvl_, (430, 400))

        screen.blit(_menu_, (180, 400))

        text = pygame.font.Font("шрифт/shrift.ttf", 40).render("You killed second boss!!!", True, (99, 221, 23))
        screen.blit(text, (250, 20))

    elif num_bos == 3:

        text = pygame.font.Font("шрифт/shrift.ttf", 40).render("You killed final boss!!!", True, (99, 221, 23))
        screen.blit(text, (250, 20))

        score = pygame.font.Font("шрифт/shrift.ttf", 45).render("+100 000 xp", True, (99, 221, 23))
        screen.blit(score, (320, 70))

        screen.blit(_menu_, (300, 500))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if num_bos == 3:
                    if 300 < event.pos[0] < 500 and 500 < event.pos[1] < 600:
                        import menu
                        menu.first_window()
                else:
                    if 180 < event.pos[0] < 380 and 400 < event.pos[1] < 500:
                        import menu
                        menu.first_window()
                    elif 430 < event.pos[0] < 630 and 400 < event.pos[1] < 500:
                        if num_bos != 3:
                            if num_bos == 1:
                                import _2_lvl
                                _2_lvl._2_lvl()
                            if num_bos == 2:
                                import _3_lvl
                                _3_lvl._3_lvl()
                                # !!!!!!!!!
        pygame.display.flip()