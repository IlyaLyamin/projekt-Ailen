import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        # создаём пулю в текущей позиции пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 12)
        self.color = (255, 10, 10)
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # отрисовываем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)