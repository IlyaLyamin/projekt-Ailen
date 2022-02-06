import pygame


class Gun():
    def __init__(self, screen, gun):
        # инициализация пушки

        self.screen = screen
        self.image = pygame.image.load(gun)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False # движение влево
        self.mleft = False # движение вправо

    def output(self):
        # рисование пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        # обновление позиции пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.5
        self.rect.centerx = self.center

    def create_gun(self):
        # размещвет пушку по центру внизу
        self.center = self.screen_rect.centerx