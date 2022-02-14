import pygame
from pygame.sprite import Group
import time
import sys

from all_sprit import stars
from skin import Skin
from gun import Gun
import music
import controls_for_bos_1
from ailens_bulet import Ailens_bullet
from time_for_play import Time
from bos import Bos
from stats_for_level import Health_and_score


def _3_lvl():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    skin = Skin(screen)
    gun = Gun(screen, skin.ret_use_skin())
    sky = stars()
    bullets = Group()

    health = Health_and_score(screen, 3)

    gun_spr = Group()
    gun_spr.add(gun)

    ino = Bos(screen, 3)
    f = True

    inos_bullets = Group()

    inos = Group()

    # time
    _time_ = Time()

    # загружаем музыку
    music.start_music(2)

    while True:
        screen.fill((0, 0, 0))
        sky.draw(screen)

        # прорисовка боса
        if (time.localtime(time.time())).tm_sec % 2 == 0 and _time_.time_for_tp:
            f = False
            inos.empty()
            ino = Bos(screen, 3)
            inos.add(ino)
            _time_.time_for_tp = False
        elif (time.localtime(time.time())).tm_sec % 2 != 0:
            _time_.time_for_tp = True

        for ino in inos.sprites():
            ino.draw_bos()
        # прорисовка пуль

        if not f:
            controls_for_bos_1.create_bos_shot(screen, _time_, ino, inos_bullets, 3)
            # bullet and gun
            controls_for_bos_1.gun_and_bullet(bullets, inos, inos_bullets, screen, _time_, gun_spr, health, 3)
            gun.output()
            gun.update_gun()

            if inos_bullets:
                for i in inos_bullets.sprites():
                    i.draw_bullet()

            controls_for_bos_1.event(gun, bullets, screen)
            health.show_health()
            pygame.display.flip()