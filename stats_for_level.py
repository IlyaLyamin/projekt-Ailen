import pygame
import pygame.font

from skin import Skin


class Health_and_score():
    def __init__(self, screen):
        self.screen = screen
        self.red_heart = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/red heart.png")
        self.green_heart = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/green heart.png")
        self.health_player = 100
        self.health_ino = 100
        skin = Skin(screen)
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

    def check_health(self):
        if self.health_player <= 0:
            print("грок мёртв")
        elif self.health_ino <= 0:
            print("инопланетянин мёртв")

    def show_health(self):
        self.screen.blit(self.red_heart, (720, 730))
        self.img_hlh_pl = pygame.font.Font('шрифт/shrift.ttf', 28).render(str(self.health_player), True, (255, 0, 0))
        self.screen.blit(self.img_hlh_pl, (680, 750))

        self.screen.blit(self.green_heart, (0, 0))
        self.img_hlh_ino = pygame.font.Font('шрифт/shrift.ttf', 28).render(str(self.health_ino), True, (99, 221, 23))
        self.screen.blit(self.img_hlh_ino, (60, 20))