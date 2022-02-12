import pygame
import pygame.font
import time


class Skin():
    def __init__(self, screen):
        self.screen = screen
        with open("xp.txt", "r")as f:
            self.money = int(f.readline())
        self.all_skin = {0: "дизайн/оружие/first.png",
                         1: "дизайн/оружие/second.png",
                         2: "дизайн/оружие/fird.png",
                         3: "дизайн/оружие/four.png",
                         4: "дизайн/оружие/beast.png"}
        self.all_pict_skin = {0: "дизайн/окно выбора скина/first.png",
                              1: "дизайн/окно выбора скина/second.png",
                              2: "дизайн/окно выбора скина/fird.png",
                              3: "дизайн/окно выбора скина/four.png",
                              4: "дизайн/окно выбора скина/five.png"}
        self.coord = [[80, 300], [330, 300], [580, 300], [80, 550], [330, 550]]
        self.all_have_skin = []
        with open("have_skin.txt", "r") as f:
            f = f.read().split()
            for i in f:
                self.all_have_skin.append(int(i))
        self.all_blocked_skin = [0, 1, 2, 3, 4]
        for i in self.all_have_skin:
            if i in self.all_blocked_skin:
                self.all_blocked_skin.remove(i)
        with open("use_skin.txt", "r") as f:
            self.use_skin = int(f.readline())

    def show_have_skins(self):
        if 0 in self.all_have_skin:
            self.screen.blit(pygame.image.load(self.all_pict_skin[0]), self.coord[0])
        if 1 in self.all_have_skin:
            self.screen.blit(pygame.image.load(self.all_pict_skin[1]), self.coord[1])
        if 2 in self.all_have_skin:
            self.screen.blit(pygame.image.load(self.all_pict_skin[2]), self.coord[2])
        if 3 in self.all_have_skin:
            self.screen.blit(pygame.image.load(self.all_pict_skin[3]), self.coord[3])
        if 4 in self.all_have_skin:
            self.screen.blit(pygame.image.load(self.all_pict_skin[4]), self.coord[4])

    def show_use_pict_skin(self):
        if 0 == self.use_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/flag.png"), (195, 305))
        if 1 == self.use_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/flag.png"), (445, 305))
        if 2 == self.use_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/flag.png"), (695, 305))
        if 3 == self.use_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/flag.png"), (195, 555))
        if 4 == self.use_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/flag.png"), (445, 555))

    def choose_use_skin(self, num):
        if num in self.all_have_skin:
            if num != self.use_skin:
                with open("use_skin.txt", "w") as f:
                    f.write(str(num))
        else:
            pass

    def show_blocked_skin(self):
        if 0 not in self.all_have_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/blocked.png"), self.coord[0])
        if 1 not in self.all_have_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/blocked.png"), self.coord[1])
        if 2 not in self.all_have_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/blocked.png"), self.coord[2])
        if 3 not in self.all_have_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/blocked.png"), self.coord[3])
        if 4 not in self.all_have_skin:
            self.screen.blit(pygame.image.load("дизайн/окно выбора скина/blocked.png"), self.coord[4])

    def buy_skin(self, num_skin):
        if num_skin not in self.all_have_skin:
            a = []
            if num_skin == 1:
                if self.money >= 10000:
                    self.all_have_skin.append(num_skin)
                    for i in self.all_have_skin:
                        a.append(str(i))
                    with open("have_skin.txt", "w") as f:
                        f.write(" ".join(a))
                        a.clear()
                    self.money -= 10000
                    with open("xp.txt", "w") as f:
                        f.write(str(self.money))
                else:
                    pass

            if num_skin == 2:
                if self.money >= 50000:
                    self.all_have_skin.append(num_skin)
                    for i in self.all_have_skin:
                        a.append(str(i))
                    with open("have_skin.txt", "w") as f:
                        f.write(" ".join(a))
                        a.clear()
                    self.money -= 50000
                    with open("xp.txt", "w") as f:
                        f.write(str(self.money))
                else:
                    pass

            if num_skin == 3:
                if self.money >= 100000:
                    self.all_have_skin.append(num_skin)
                    for i in self.all_have_skin:
                        a.append(str(i))
                    with open("have_skin.txt", "w") as f:
                        f.write(" ".join(a))
                        a.clear()
                    self.money -= 100000
                    with open("xp.txt", "w") as f:
                        f.write(str(self.money))
                else:
                    pass

            if num_skin == 4:
                if self.money >= 500000:
                    self.all_have_skin.append(num_skin)
                    for i in self.all_have_skin:
                        a.append(str(i))
                    with open("have_skin.txt", "w") as f:
                        f.write(" ".join(a))
                        a.clear()
                    self.money -= 500000
                    with open("xp.txt", "w") as f:
                        f.write(str(self.money))
                else:
                    pass
        else:
            pass

    def can_buy(self, num_skin):
        pygame.font.init()
        if num_skin not in self.all_have_skin:
            if num_skin == 1:
                if self.money >= 10000:
                    pass
                else:
                    text = pygame.font.Font('шрифт/shrift.ttf', 58).render("not enought xp", True, (255, 0, 0))
                    self.screen.blit(text, (250, 200))
            if num_skin == 2:
                if self.money >= 50000:
                    pass
                else:
                    text = pygame.font.Font('шрифт/shrift.ttf', 58).render("not enought xp", True, (255, 0, 0))
                    self.screen.blit(text, (250, 200))
            if num_skin == 3:
                if self.money >= 100000:
                    pass
                else:
                    text = pygame.font.Font('шрифт/shrift.ttf', 58).render("not enought xp", True, (255, 0, 0))
                    self.screen.blit(text, (250, 200))
            if num_skin == 4:
                if self.money >= 500000:
                    pass
                else:
                    text = pygame.font.Font('шрифт/shrift.ttf', 58).render("not enought xp", True, (255, 0, 0))
                    self.screen.blit(text, (250, 200))

    def ret_use_skin(self):
        if self.use_skin == 0:
            return "дизайн/оружие/first.png"
        if self.use_skin == 1:
            return "дизайн/оружие/second.png"
        if self.use_skin == 2:
            return "дизайн/оружие/fird.png"
        if self.use_skin == 3:
            return "дизайн/оружие/fourt.png"
        if self.use_skin == 4:
            return "дизайн/оружие/beast.png"