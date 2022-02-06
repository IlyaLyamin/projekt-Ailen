import pygame.font


class Scores():
    # вывод игровой информации
    def __init__(self, screen, stats):
        # инициализируем подсчёт очков
        pygame.font.init()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (99, 221, 23)
        # текущий счёт
        self.font = pygame.font.Font('шрифт/shrift.ttf', 28)

        self.image_wave()
        self.show_wave()

        self.image_hight_score()

        self.image_score()

        self.image_your_score()
        self.show_your_score()

    def image_score(self):
        # преобразует текст счёта в изображение
        self.score_img = self.font.render("+ " + str(self.stats.score_now), True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 50

    def show_score(self):
        # отображение счёта
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hight_score_img, self.hight_score_rect)

    def image_your_score(self):
        self.your_score_img = self.font.render("YOUR SCORE: " + str(self.stats.score_now), True, self.text_color)
        self.your_score_rect = self.your_score_img.get_rect()
        self.your_score_rect.right = 465
        self.your_score_rect.top = 315

    def show_your_score(self):
        self.screen.blit(self.your_score_img, self.your_score_rect)

    def image_hight_score(self):
        # преобразует рекорд в графическое изображене
        self.hight_score_img = self.font.render("RECORD: " + str(self.stats.hight_record), True, self.text_color)
        self.hight_score_rect = self.hight_score_img.get_rect()
        self.hight_score_rect.right = 780
        self.hight_score_rect.top = 20

    def image_wave(self):
        self.wave_img = self.font.render(str(self.stats.wave) + " WAVE", True, self.text_color)
        self.wave_rect = self.wave_img.get_rect()
        self.wave_rect.x = 400
        self.wave_rect.y = 20

    def show_wave(self):
        self.screen.blit(self.wave_img, self.wave_rect)