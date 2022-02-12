import pygame
import sys
import time

from bos_1 import Bos_1_
from bullet import Bullet
from controls_for_free_play import pause
from ailens_bulet import Ailens_bullet
from time_for_play import Time


def event(gun, bullets, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_e:
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
            elif event.key == pygame.K_ESCAPE:
                pause()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                gun.mleft = False
            elif event.key == pygame.K_d:
                gun.mright = False


def create_bos_shot(screen, _time_, ino, inos_bullets):
    if 0.25 < time.time() - int(time.time()) < 0.7 and _time_.time_for_shot:
        new_ailens_bullet = Ailens_bullet(screen, ino)
        inos_bullets.add(new_ailens_bullet)
        _time_.time_for_shot = False
    elif 0.7 < time.time() - int(time.time()) < 0.9:
        _time_.time_for_shot = True


def gun_and_bullet(bullets, inos, inos_bullets, screen, _time_, gun, health):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    bullets.update()
    inos_bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, inos, True, False)
    if collision:
        health.health_ino -= health.uron_player
        health.check_health()
        print(health.health_ino)
    collision_2 = pygame.sprite.groupcollide(inos_bullets, gun, True, False)
    if collision_2:
        health.health_player -= 5
        health.check_health()
        print(health.health_player)