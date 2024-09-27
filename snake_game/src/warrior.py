import pygame, random
from rand import RAND
from data import DATA
from param import PARAMETR


# рисует иницилизирует и размещает фрукты(войнов)
class WARRIOR():

    def __init__(self):
        self.randomize(PARAMETR.parametr)
        self.ran = RAND()

    def randomize(self, value):
        if value == 1:
            self.lvl1_spawn()
        if value == 2:
            self.lvl2_spawn()
        if value == 3:
            self.lvl3_spawn()
        if value == 4:
            self.lvl4_spawn()
        if value == 5:
            self.lvl5_spawn()
        self.pos = pygame.math.Vector2(self.x, self.y)

    def lvl1_spawn(self):
        self.x = random.randint(0, DATA.block_count_width - 1)
        self.y = random.randint(0, DATA.block_count_hight - 1)

    def lvl2_spawn(self):
        ranges_x = [(0, 7), (9, 1.7 * DATA.ten), (1.9 * DATA.ten, DATA.block_count_width - 1)]
        ne_ranges_x = [(8, 8), (1.8 * DATA.ten, 1.8 * DATA.ten)]
        ranges_y = [(0, DATA.block_count_hight - 1)]
        self.x = self.ran.random_in_range_x(ranges_x or ne_ranges_x)
        if self.ran.is_in_ranges(self.x, ranges_x):
            self.y = self.ran.random_in_range_y(ranges_y)
        if self.ran.is_in_ranges(self.x, ne_ranges_x):
            ranges_y = [(0, 1), (8, 8)]
            self.y = self.ran.random_in_range_y(ranges_y)

    def lvl3_spawn(self):
        ranges_x = [(0, 9), (1.1 * DATA.ten, 1.5 * DATA.ten), (1.7 * DATA.ten, DATA.block_count_width - 1)]
        ne_ranges_x = [(DATA.ten, DATA.ten), (1.6 * DATA.ten, 1.6 * DATA.ten), (2.2 * DATA.ten, 2.2 * DATA.ten)]
        ranges_y = [(0, DATA.block_count_hight - 1)]
        self.x = self.ran.random_in_range_x(ranges_x or ne_ranges_x)
        if self.ran.is_in_ranges(self.x, ranges_x):
            self.y = self.ran.random_in_range_y(ranges_y)
        if self.ran.is_in_ranges(self.x, ne_ranges_x):
            ranges_y = [(0, 3), (1.3 * DATA.ten, DATA.block_count_hight - 1)]
            self.y = self.ran.random_in_range_y(ranges_y)

    def lvl4_spawn(self):
        ranges_x = [(0, 9), (1.1 * DATA.ten, 1.5 * DATA.ten), (1.7 * DATA.ten, DATA.block_count_width - 1)]
        ne_ranges_x_1 = [(8, 8)]
        ne_ranges_x_2 = [(2.2 * DATA.ten, 2.2 * DATA.ten)]
        ranges_y = [(0, DATA.block_count_hight - 1)]
        self.x = self.ran.random_in_range_x(ranges_x or ne_ranges_x_1 or ne_ranges_x_2)
        if self.ran.is_in_ranges(self.x, ranges_x):
            self.x = self.ran.random_in_range_x(ranges_x)
            self.y = self.ran.random_in_range_y(ranges_y)
        if self.ran.is_in_ranges(self.x, ne_ranges_x_1):
            ranges_y = [(0, 1)]
            self.x = self.ran.random_in_range_x(ne_ranges_x_1)
            self.y = self.ran.random_in_range_y(ranges_y)
        if self.ran.is_in_ranges(self.x, ne_ranges_x_2):
            ranges_y = [(DATA.block_count_hight - 2, DATA.block_count_hight - 1)]
            self.x = self.ran.random_in_range_x(ne_ranges_x_2)
            self.y = self.ran.random_in_range_y(ranges_y)

    def lvl5_spawn(self):
        ranges_x = [(0, 9), (1.1 * DATA.ten, 1.5 * DATA.ten), (1.7 * DATA.ten, DATA.block_count_width - 1)]
        ne_ranges_x_1 = [(8, 8)]
        ne_ranges_x_2 = [(1.2 * DATA.ten, 2.7 * DATA.ten)]
        ne_ranges_x_3 = [(2.8 * DATA.ten, 2.8 * DATA.ten)]
        ranges_y = [(0, DATA.block_count_hight - 1)]
        self.x = self.ran.random_in_range_x(ranges_x or ne_ranges_x_1 or ne_ranges_x_2 or ne_ranges_x_3)
        if self.ran.is_in_ranges(self.x, ranges_x):
            self.y = self.ran.random_in_range_y(ranges_y)
        if self.ran.is_in_ranges(self.x, ne_ranges_x_1):
            ranges_y = [(0, 1), (6, 1.1 * DATA.ten), (DATA.block_count_hight - 2, DATA.block_count_hight - 1)]
            self.y = self.ran.random_in_range_y(ranges_y)
        if self.ran.is_in_ranges(self.x, ne_ranges_x_2):
            ranges_y = [(0, 2), (4, 1.3 * DATA.ten), (DATA.block_count_hight - 3, DATA.block_count_hight - 1)]
            self.y = self.ran.random_in_range_y(ranges_y)
        if self.ran.is_in_ranges(self.x, ne_ranges_x_3):
            ranges_y = [(0, 2), (DATA.block_count_hight - 3, DATA.block_count_hight - 1)]
            self.y = self.ran.random_in_range_y(ranges_y)

    def draw_warrior(self):
        warrior = pygame.Rect(int(self.pos.x * DATA.block_size), int(self.pos.y * DATA.block_size), DATA.block_size,
                              DATA.block_size)
        pygame.draw.rect(DATA.window, DATA.warrior_color, warrior)
