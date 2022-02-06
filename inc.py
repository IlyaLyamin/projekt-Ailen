import pygame


class Ino(pygame.sprite.Sprite):
    # класс одного пришельца

    def __init__(self, screen, speed):
        # инициализируем и задаём начальную позицию
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("дизайн/инопланетяни, бонцсы и т.д/инопланетянин_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.speed = speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        # вывод пришельца на экран
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
