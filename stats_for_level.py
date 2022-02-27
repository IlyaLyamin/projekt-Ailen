import pygame
import pygame.font

from skin import Skin
from stats import Stats


class Health_and_score():
    def __init__(self, screen, lvl):
        self.lvl = lvl
        self.screen = screen
        self.red_heart = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/red heart.png")
        self.green_heart = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/green heart.png")

        self.health_player = 100

        if self.lvl == 1:
            self.health_ino = 100
        elif self.lvl == 2:
            self.health_ino = 300
        elif self.lvl == 3:
            self.health_ino = 500

        skin = Skin(screen)

        if self.lvl == 1:
            if skin.use_skin == 0:
                self.uron_player = 1
            elif skin.use_skin == 1:
                self.uron_player = 2
            elif skin.use_skin == 2:
                self.uron_player = 4
            elif skin.use_skin == 3:
                self.uron_player = 8
            elif skin.use_skin == 4:
                self.uron_player = 10
        else:
            if skin.use_skin == 0:
                self.uron_player = 1
            elif skin.use_skin == 1:
                self.uron_player = 2
            elif skin.use_skin == 2:
                self.uron_player = 3
            elif skin.use_skin == 3:
                self.uron_player = 4
            elif skin.use_skin == 4:
                self.uron_player = 5

        if self.lvl == 1:
            self.uron_ino = 5
        elif self.lvl == 2:
            self.uron_ino = 5
        else:
            self.uron_ino = 10

    def check_health(self):
        if self.health_player <= 0:
            import between_lvl_lose
            between_lvl_lose.between_bos_lose()
        elif self.health_ino <= 0:
            a = Stats()
            with open("xp.txt", "w") as f:
                if self.lvl == 1:
                    a.all_score += 10000
                if self.lvl == 2:
                    a.all_score += 50000
                if self.lvl == 3:
                    a.all_score += 100000
                f.write(str(a.all_score))
            with open("for_level.txt", "w") as f:
                if self.lvl == 1:
                    a.all_points += 10000
                if self.lvl == 2:
                    a.all_points += 50000
                if self.lvl == 3:
                    a.all_points += 100000
                f.write(str(a.all_score))
            import between_lvl_win
            between_lvl_win.between_bos_win(self.lvl)

    def show_health(self):
        self.screen.blit(self.red_heart, (720, 730))
        self.img_hlh_pl = pygame.font.Font('шрифт/shrift.ttf', 28).render(str(self.health_player), True, (255, 0, 0))
        self.screen.blit(self.img_hlh_pl, (680, 750))

        self.screen.blit(self.green_heart, (0, 0))
        self.img_hlh_ino = pygame.font.Font('шрифт/shrift.ttf', 28).render(str(self.health_ino), True, (99, 221, 23))
        self.screen.blit(self.img_hlh_ino, (60, 20))