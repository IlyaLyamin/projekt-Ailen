class Stats():
    # статистика для свободной игры
    def __init__(self):
        # инициализируем
        self.reset_stats()
        self.run_game = True
        self.speed = 0.04
        self.end_score = 0
        self.wave = 0
        with open("for_level.txt", "r") as f:
            self.all_points = int(f.readline())
        with open("for_level.txt", "r") as f:
            f = int(f.readline())
            if f < 10000:
                self.lvl = 1
            else:
                self.lvl = f // 10000
        with open("xp.txt", "r") as f:
            self.all_score = int(f.readline())
        with open("rec.txt", "r") as f:
            self.hight_record = int(f.readline())

    def reset_stats(self):
        # статистика изменяющаяся во время игры
        self.guns_left = 0
        self.score_now = 0