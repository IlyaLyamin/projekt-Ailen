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
    DISP_FIRST = pygame.display.set_mode((800, 800))
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

    # добавление звёзд
    for i in range(150):
        star = pygame.sprite.Sprite(all_star_sprites)
        star.image = pygame.image.load("дизайн/главное окно/звезда.png")
        star.rect = star.image.get_rect()
        star.rect.x = random.randrange(800)
        star.rect.y = random.randrange(800)

    while True:
        all_star_sprites.draw(screen)
        all_btn_sprites.draw(screen)
        DISP_FIRST.blit(fon, (300, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 200 < event.pos[0] < 600 and 250 < event.pos[1] < 400:
                    Ailen.run("дизайн/задний фон/_1.jpg", "дизайн/оружие/beast.png")
                    print("ok")
                    sys.exit()

        pygame.display.flip()


first_window()