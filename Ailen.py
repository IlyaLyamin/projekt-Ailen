import pygame
from gun import Gun
import controls


def run(type_fons, type_guns):

    pygame.init()
    w = 700
    h = 900
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
        pygame.display.flip()


run("дизайн/задний фон/_1.jpg", "дизайн/оружие/blue gun.png")