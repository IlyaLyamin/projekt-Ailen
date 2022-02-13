import pygame
import sys
import pygame.font

import all_sprit


def before_first_bos():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    # звёзды
    stars = all_sprit.stars()
    stars.draw(screen)

    # копка меню
    _menu_ = pygame.transform.scale(pygame.image.load("дизайн/game over/menu.png"), (100, 50))
    screen.blit(_menu_, (20, 20))

    # кнопка play
    _play_ = pygame.image.load("дизайн/управление/play.png")
    screen.blit(_play_, (250, 600))

    # надпись левела
    _lvl_ = pygame.image.load("дизайн/уровни/1_level.png")
    screen.blit(_lvl_, (180, 20))

    #текст
    y = 110
    text = ["Welcome to the story game mode,",
            "here you will have to fight the",
            "strongest bosses of the cosmos",
            "at each level. Why they are the",
            "strongest you will find out during",
            "the game, for each boss you will",
            "be awarded 'xp'. Have a nice game",
            "                 and good luck."]
    for i in text:
        text_img = pygame.font.Font("шрифт/shrift.ttf", 40).render(str(i), True, (99, 221, 23))
        y += 50
        screen.blit(text_img, (170, y))

    pygame.mixer.music.stop()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 20 < event.pos[0] < 120 and 20 < event.pos[1] < 70:
                    import menu
                    menu.first_window()
                elif 250 < event.pos[0] < 450 and 600 < event.pos[1] < 700:
                    import _1_lvl
                    _1_lvl._1_lvl()
        pygame.display.flip()


before_first_bos()