import pygame
import sys
import controls
import Ailen
import random


def first_window():
    pygame.init()

    # добавление головы инопланетянина
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")
    fon = pygame.image.load("дизайн/главное окно/инопланетянин.png")

    # создание спрайтов
    all_star_sprites = pygame.sprite.Group()
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

    # надписи
    lvl_ = pygame.image.load("дизайн/главное окно/lvl.png")
    lvl = pygame.transform.scale(lvl_, (80, 50))
    ex_ = pygame.image.load("дизайн/главное окно/ex.png")
    ex = pygame.transform.scale(ex_, (80, 40))

    # добавление звёзд
    for i in range(150):
        star = pygame.sprite.Sprite(all_star_sprites)
        star.image = pygame.image.load("дизайн/главное окно/звезда.png")
        star.rect = star.image.get_rect()
        star.rect.x = random.randrange(800)
        star.rect.y = random.randrange(800)

    # загружаем музыку
    vol = 1.0
    flPause_menu = True
    pygame.mixer.music.load("музыка/первый уровень.mp3")
    pygame.mixer.music.play(-1)

    while True:
        all_star_sprites.draw(screen)
        all_btn_sprites.draw(screen)
        screen.blit(lvl, (580, 50))
        screen.blit(fon, (300, 50))
        screen.blit(ex, (580, 0))
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
                    Ailen.run("дизайн/задний фон/_1.jpg", "дизайн/оружие/beast.png")
                    sys.exit()
                elif 200 < event.pos[0] < 600 and 420 < event.pos[1] < 620:
                    screen.fill("black", (0, 0, 800, 800))
                    control_file.control_window()
                    return
        screen.blit(unwatching_din.image, unwatching_din.rect)
        if flPause_menu:
            screen.blit(music_on_sprite.image, music_on_sprite.rect)
        else:
            screen.blit(turn_of_dinamik.image, turn_of_dinamik.rect)

        pygame.display.flip()


first_window()