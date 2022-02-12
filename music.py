import pygame


def start_music(num):
    if num == 0:
        pygame.mixer.music.load("музыка/меню.mp3")
        pygame.mixer.music.play(-1)
    if num == 1:
        pygame.mixer.music.load("музыка/первый уровень.mp3")
        pygame.mixer.music.play(-1)
    if num == 2:
        pygame.mixer.music.load("музыка/сюжет_1.mp3")
        pygame.mixer.music.play(-1)
    if num == 3:
        pass


def draw_pause(screen):
    pygame.mixer.music.pause()
    _un_dinamic_ = pygame.image.load("дизайн/главное окно/выключенный динамик.png")
    screen.blit(_un_dinamic_, (20, 20))


def draw_unpause(screen):
    pygame.mixer.music.unpause()
    _black_din_ = pygame.image.load("дизайн/главное окно/чёрная колонка.png")
    screen.blit(_black_din_, (20, 20))
    _dinamic_ = pygame.image.load("дизайн/главное окно/люченный динамик.png")
    screen.blit(_dinamic_, (20, 20))