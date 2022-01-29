import pygame
import sys
import controls
import random
from gun import Gun


def music(screen, pause):

    # добавление кнопки колонки
    music_on_sprite = pygame.sprite.Sprite()
    music_on_sprite.image = pygame.image.load("дизайн/главное окно/люченный динамик.png")
    music_on_sprite.rect = music_on_sprite.image.get_rect()
    music_on_sprite.rect.x = 20
    music_on_sprite.rect.y = 20

    turn_of_dinamik = pygame.sprite.Sprite()
    turn_of_dinamik.image = pygame.image.load("дизайн/главное окно/выключенный динамик.png")
    turn_of_dinamik.rect = turn_of_dinamik.image.get_rect()
    turn_of_dinamik.rect.x = 20
    turn_of_dinamik.rect.y = 20

    unwatching_din = pygame.sprite.Sprite()
    unwatching_din.image = pygame.image.load("дизайн/главное окно/чёрная колонка.png")
    unwatching_din.rect = unwatching_din.image.get_rect()
    unwatching_din.rect.x = 20
    unwatching_din.rect.y = 20

    screen.blit(unwatching_din.image, unwatching_din.rect)
    if pause:
        screen.blit(music_on_sprite.image, music_on_sprite.rect)
    else:
        screen.blit(turn_of_dinamik.image, turn_of_dinamik.rect)


def stars(screen):
    # добавление звёзд
    all_star_sprites = pygame.sprite.Group()
    for i in range(150):
        star = pygame.sprite.Sprite(all_star_sprites)
        star.image = pygame.image.load("дизайн/главное окно/звезда.png")
        star.rect = star.image.get_rect()
        star.rect.x = random.randrange(800)
        star.rect.y = random.randrange(800)
    all_star_sprites.draw(screen)


def free_run(type_fons, type_guns):
    pygame.init()
    w = 800
    h = 800
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Ailen")
    DISPLAYSURF = pygame.display.set_mode((w, h))
    gun = Gun(screen, type_guns)
    # загрузка изображения
    fon = pygame.image.load(type_fons)

    while True:
        controls.events(gun)
        gun.update_gun()
        DISPLAYSURF.blit(fon, (-100, -300))
        gun.output()
        music(screen, True)
        pygame.display.flip()


def control_window():
    # создание окна
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    # добавление звёзд
    stars(screen)

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < event.pos[0] < 550 and 650 < event.pos[1] < 750:
                    free_run("дизайн/задний фон/_1.jpg", "дизайн/оружие/first.png")
                    sys.exit()
                elif 750 < event.pos[0] < 790 and 10 < event.pos[1] < 50:
                    first_window()
                    sys.exit()
        pygame.display.flip()


def first_window():
    pygame.init()

    # добавление головы инопланетянина
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")
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

    # надписи
    lvl_ = pygame.image.load("дизайн/главное окно/lvl.png")
    lvl = pygame.transform.scale(lvl_, (80, 50))
    ex_ = pygame.image.load("дизайн/главное окно/ex.png")
    ex = pygame.transform.scale(ex_, (80, 40))

    # добавление звёзд
    stars(screen)

    # загружаем музыку
    vol = 1.0
    flPause_menu = True
    pygame.mixer.music.load("музыка/меню.mp3")
    pygame.mixer.music.play(-1)

    while True:
        all_btn_sprites.draw(screen)
        screen.blit(lvl, (580, 50))
        screen.blit(fon, (300, 50))
        screen.blit(ex, (580, 0))
        screen.blit(_FREE_PLAY_, (200, 590))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if flPause_menu:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    flPause_menu = not flPause_menu
                elif event.key == pygame.K_DOWN:
                    vol -= 0.1
                    pygame.mixer.music.set_volume(vol)
                elif event.key == pygame.K_UP:
                    vol += 0.1
                    pygame.mixer.music.set_volume(vol)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 200 < event.pos[0] < 600 and 250 < event.pos[1] < 400:
                    pygame.mixer.music.stop()
                    control_window()
                    sys.exit()
                elif 200 < event.pos[0] < 600 and 420 < event.pos[1] < 620:# choose skin
                    pass
                elif 200 < event.pos[0] < 600 and 590 < event.pos[1] < 790:
                    pygame.mixer.music.stop()
                    control_window()
                    sys.exit()
        music(screen, flPause_menu)

        pygame.display.flip()


first_window()