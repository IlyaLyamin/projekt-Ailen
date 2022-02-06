import pygame
import random
import pygame.font

from stats import Stats
from scores import Scores


def stars():
    # добавление звёзд
    all_star_sprites = pygame.sprite.Group()
    for i in range(150):
        star = pygame.sprite.Sprite(all_star_sprites)
        star.image = pygame.image.load("дизайн/главное окно/звезда.png")
        star.rect = star.image.get_rect()
        star.rect.x = random.randrange(800)
        star.rect.y = random.randrange(800)
    return all_star_sprites


def create_menu(screen):
    # добавление головы инопланетянина
    fon = pygame.image.load("дизайн/главное окно/инопланетянин.png")

    # создание спрайтов
    all_btn_sprites = pygame.sprite.Group()

    # добавление кнопки "играть"
    play_sprite = pygame.sprite.Sprite()
    play_btn = pygame.image.load("дизайн/главное окно/кнопка play.png")
    play_sprite.image = (pygame.transform.scale(play_btn, (400, 150)))
    play_sprite.rect = play_sprite.image.get_rect()
    play_sprite.rect.x = 200
    play_sprite.rect.y = 250
    all_btn_sprites.add(play_sprite)

    # добавление кнопки "выбрать скин"
    chose_skin_sprite = pygame.sprite.Sprite()
    chose_skin = pygame.image.load("дизайн/главное окно/кнопка ch skin.png")
    chose_skin_sprite.image = (pygame.transform.scale(chose_skin, (400, 150)))
    chose_skin_sprite.rect = chose_skin_sprite.image.get_rect()
    chose_skin_sprite.rect.x = 200
    chose_skin_sprite.rect.y = 420
    all_btn_sprites.add(chose_skin_sprite)

    # добавление кнопки "свободная игра"
    _FREE_1_PLAY_ = pygame.image.load("дизайн/главное окно/кнопка free play.png")
    _FREE_PLAY_ = pygame.transform.scale(_FREE_1_PLAY_, (400, 150))

    # добавление звёзд
    stars().draw(screen)

    all_btn_sprites.draw(screen)
    screen.blit(fon, (300, 50))
    screen.blit(_FREE_PLAY_, (200, 590))

    stats = Stats()

    pygame.font.init()
    all_score = pygame.font.Font('шрифт/shrift.ttf', 34).render("xp:" + str(stats.all_score), True, (99, 221, 23))
    all_score_rect = all_score.get_rect()
    all_score_rect.right = 790
    all_score_rect.top = 0

    screen.blit(all_score, all_score_rect)

    lvl = pygame.font.Font('шрифт/shrift.ttf', 34).render("lvl: " + str(stats.lvl), True, (99, 221, 23))
    lvl_rect = lvl.get_rect()
    lvl_rect.right = 790
    lvl_rect.top = 30

    screen.blit(lvl, lvl_rect)


def create_window_control(screen):

    # добавление звёзд
    stars().draw(screen)

    # загрузка
    _Q_ = pygame.image.load("дизайн/управление/кнопка Q.png")
    _SPACE_ = pygame.image.load("дизайн/управление/кнопка пробел.png")
    _A_ = pygame.image.load("дизайн/управление/кнопка A.png")
    _D_ = pygame.image.load("дизайн/управление/кнопка D.png")
    _UP_ = pygame.image.load("дизайн/управление/кнопка up.png")
    _DOWN_ = pygame.image.load("дизайн/управление/кнопка down.png")

    _MUSIC_ = pygame.image.load("дизайн/управление/music.png")
    _MOVE_LEFT_ = pygame.image.load("дизайн/управление/move left.png")
    _MOVE_RIGHT_ = pygame.image.load("дизайн/управление/move right.png")

    _UP_MUSIC_ = pygame.image.load("дизайн/управление/up music.png")
    _DOWN_MUSIC_ = pygame.image.load("дизайн/управление/down music.png")

    _SHOT_ = pygame.image.load("дизайн/управление/shot.png")

    _PLAY_ = pygame.image.load("дизайн/управление/play.png")
    _STRING_ = pygame.image.load("дизайн/управление/good play.png")

    _KREST_1_ = pygame.image.load("дизайн/управление/krest.png")
    _KREST_ = pygame.transform.scale(_KREST_1_, (40, 40))

    # прорисовка кнопок и описания
    screen.blit(_Q_, (50, 30))
    screen.blit(_A_, (50, 140))
    screen.blit(_D_, (50, 250))

    screen.blit(_UP_, (500, 30))
    screen.blit(_DOWN_, (500, 140))

    screen.blit(_SPACE_, (50, 360))

    # надписи
    screen.blit(_MUSIC_, (160, 55))
    screen.blit(_MOVE_LEFT_, (160, 155))
    screen.blit(_MOVE_RIGHT_, (160, 255))

    screen.blit(_UP_MUSIC_, (610, 31))
    screen.blit(_DOWN_MUSIC_, (610, 141))

    screen.blit(_SHOT_, (310, 365))

    screen.blit(_STRING_, (150, 550))
    screen.blit(_PLAY_, (250, 650))

    screen.blit(_KREST_, (750, 10))