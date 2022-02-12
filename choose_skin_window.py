import pygame
import sys
import pygame.font
import time

import music
import all_sprit
import stats
from skin import Skin


def create_choose_skin_window():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    _menu_ = pygame.transform.scale(pygame.image.load("дизайн/окно выбора скина/menu.png"), (100, 50))

    stars = all_sprit.stars()

    mouse_x = 0
    mouse_y = 0

    _music_ = True

    while True:
        skin = Skin(screen)
        screen.fill((0, 0, 0))
        stars.draw(screen)
        if _music_:
            music.draw_unpause(screen)
        else:
            music.draw_pause(screen)

        # прорисовка цен
        if 1 not in skin.all_have_skin:
            sale_1 = pygame.font.Font('шрифт/shrift.ttf', 34).render("10 000 xp", True, (99, 221, 23))
            screen.blit(sale_1, (345, 465))
        if 2 not in skin.all_have_skin:
            sale_1 = pygame.font.Font('шрифт/shrift.ttf', 34).render("50 000 xp", True, (99, 221, 23))
            screen.blit(sale_1, (600, 465))
        if 3 not in skin.all_have_skin:
            sale_1 = pygame.font.Font('шрифт/shrift.ttf', 34).render("100 000 xp", True, (99, 221, 23))
            screen.blit(sale_1, (92, 715))
        if 4 not in skin.all_have_skin:
            sale_1 = pygame.font.Font('шрифт/shrift.ttf', 34).render("500 000 xp", True, (99, 221, 23))
            screen.blit(sale_1, (345, 715))

        # прорисовка скинов
        skin.show_have_skins()
        skin.show_use_pict_skin()
        skin.show_blocked_skin()

        # menu
        screen.blit(_menu_, (690, 20))

        # счёт кошелька
        with open("xp.txt", "r") as f:
            money = int(f.readline())
        money_img = pygame.font.Font('шрифт/shrift.ttf', 40).render("XP: " + str(money), True, (99, 221, 23))
        money_rect = money_img.get_rect()
        money_rect.centerx = 400
        money_rect.top = 100
        screen.blit(money_img, money_rect)

        # отработка возможности покупки
        if 330 < mouse_x < 480 and 300 < mouse_y < 470:
            skin.can_buy(1)
        elif 580 < mouse_x < 730 and 300 < mouse_y < 470:
            skin.can_buy(2)
        elif 80 < mouse_x < 230 and 550 < mouse_y < 720:
            skin.can_buy(3)
        elif 330 < mouse_x < 480 and 550 < mouse_y < 720:
            skin.can_buy(4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.mixer.music.pause()
                    _music_ = False
                elif event.key == pygame.K_e:
                    pygame.mixer.music.unpause()
                    _music_ = True
            elif event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 80 < mouse_x < 230 and 300 < mouse_y < 470:
                    skin.choose_use_skin(0)
                elif 330 < mouse_x < 480 and 300 < mouse_y < 470:
                    skin.buy_skin(1)
                    skin.choose_use_skin(1)
                elif 580 < mouse_x < 730 and 300 < mouse_y < 470:
                    skin.buy_skin(2)
                    skin.choose_use_skin(2)
                elif 80 < mouse_x < 230 and 550 < mouse_y < 720:
                    skin.buy_skin(3)
                    skin.choose_use_skin(3)
                elif 330 < mouse_x < 480 and 550 < mouse_y < 720:
                    skin.buy_skin(4)
                    skin.choose_use_skin(4)
                elif 690 < mouse_x < 790 and 20 < mouse_y < 70:
                    import menu
                    menu.first_window()

        pygame.display.flip()