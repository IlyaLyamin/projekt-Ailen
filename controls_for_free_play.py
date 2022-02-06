import pygame
import sys
import pygame.font

import music
from bullet import Bullet
from inc import Ino
import time
from stats import Stats


def events_free_play(gun, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # контроль музыки
            if event.key == pygame.K_q:
                music.draw_pause(screen)
            elif event.key == pygame.K_e:
                music.draw_unpause(screen)
            # контрль пушки
            elif event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            # выстрел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
            # пауза
            elif event.key == pygame.K_ESCAPE:
                pause()
        # контроль пушки
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update_inos(stats, screen, gun, inos, bullets, sc):
    # обновляет позицию инопланетян
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets, sc)
    inos_check(stats, screen, gun, inos, bullets, sc)


def update(sky, screen, gun, bullets, inos, stats, sc):
    # обновление экрана
    screen.fill((0, 0, 0))
    sky.draw(screen)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)

    sc.image_wave()
    sc.show_wave()

    pygame.display.flip()


def update_bullets(screen, inos, bullets, stats, sc):
    # обновляет позицию пули
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collision:
        stats.score_now += 1 * stats.wave
        stats.all_score += 1 * stats.wave
        stats.all_points += 1 * stats.wave
        with open("xp.txt", "w") as f:
            f.write(str(stats.all_score))
        with open("for_level.txt", "w") as f:
            f.write(str(stats.all_points))
        sc.image_score()
        check_record(stats, sc)
    if len(inos) == 0:
        bullets.empty()
        create_arm(screen, inos, "win", stats, sc)


def inos_check(stats, screen, gun, inos, bullets, sc):
    # проверка, добрались ли пришельцы до линии пушки
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom - 145:
            gun_kill(stats, screen, gun, inos, bullets, sc)
            break


def create_arm(screen, inos, res, stats, sc):
    stats.wave += 1
    # создание армии пришельцев
    if res == "win":
        stats.speed += 0.01
    ino = Ino(screen, stats.speed)
    ino_width = ino.rect.width
    num_ino_x = int((800 - (2 * ino_width)) / ino_width) - 1
    ino_height = ino.rect.height
    num_ino_y = int(((800 - 200 - (2 * ino_height)) / ino_height)) - 1

    for row_num in range(num_ino_y):
        for ino_num in range(num_ino_x):
            ino = Ino(screen, stats.speed)
            ino.x = (ino_width * 2) + ino_width * ino_num
            ino.y = ino_height + ino_height * row_num
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_num
            inos.add(ino)


def gun_kill(stats, screen, gun, inos, bullets, sc):
    # столкновение пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -= 1
        inos.empty()
        bullets.empty()
        create_arm(screen, inos, "lose", stats, sc)
        gun.create_gun()
        time.sleep(1)
    else:
        pygame.mixer.music.stop()
        import game_over
        game_over.game_over_window(sc)
        stats.run_game = False
        sys.exit()


def check_record(stats, sc):
    # проверка рекорда
    if stats.score_now > stats.hight_record:
        stats.hight_record = stats.score_now
        with open("rec.txt", "w") as f:
            f.write(str(stats.hight_record))
    sc.image_hight_score()


def pause():
    paused = True
    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    pygame.mixer.music.unpause()