import pygame
import sys

import all_sprit
from stats import Stats
from scores import Scores


def game_over_window(sc):
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    all_sprit.stars().draw(screen)

    _ailen_ = pygame.image.load("дизайн/game over/инопланетянин.png")
    screen.blit(_ailen_, (312, 30))

    _game_over_ = pygame.image.load("дизайн/game over/game over.png")
    screen.blit(_game_over_, (200, 170))

    _play_again_ = pygame.image.load("дизайн/game over/play again.png")
    screen.blit(_play_again_, (302, 370))

    _menu_ = pygame.image.load("дизайн/game over/menu.png")
    screen.blit(_menu_, (302, 500))

    sc.image_your_score()
    sc.show_your_score()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 302 < event.pos[0] < 502 and 370 < event.pos[1] < 470:
                    import free_play
                    free_play.run()
                    print("play again")
                elif 302 < event.pos[0] < 502 and 500 < event.pos[1] < 600:
                    import menu
                    menu.first_window()
                    print("menu")
        pygame.display.flip()