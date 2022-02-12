import pygame

from all_sprit import stars
import music
from controls_for_free_play import events_free_play, update, update_bullets
from controls_for_free_play import update_inos
from gun import Gun
from pygame.sprite import Group
from skin import Skin
from stats import Stats
from scores import Scores


def run():

    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")
    skin = Skin(screen)
    gun = Gun(screen, skin.ret_use_skin())

    sky = stars()
    inos = Group()
    stats = Stats()
    sc = Scores(screen, stats)

    # музыка
    music.start_music(1)
    music.draw_unpause(screen)

    #
    bullets = Group()

    while True:
        events_free_play(gun, screen, bullets)
        gun.update_gun()
        update(sky, screen, gun, bullets, inos, stats, sc)
        update_bullets(screen, inos, bullets, stats, sc)
        update_inos(stats, screen, gun, inos, bullets, sc)