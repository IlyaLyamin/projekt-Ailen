import pygame


class Ailens_bullet(pygame.sprite.Sprite):

    def __init__(self, screen, ino, lvl):
        super(Ailens_bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 10)
        self.color = (0, 255, 0)
        if lvl == 1:
            self.speed = 2.0
        if lvl == 2:
            self.speed = 4.0
        if lvl == 3:
            self.speed = 8.0
        self.rect.centerx = ino.rect.centerx
        self.rect.bottom = ino.rect.bottom
        self.y = float(self.rect.y)

    def update(self):
        # перемещение пули вниз
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # отрисовываем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)