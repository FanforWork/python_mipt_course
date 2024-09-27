import pygame
import random
from data import DATA


# это класс ответсвенный за бонусы(друиды)
class BONUS:
    def __init__(self):
        self.random_bonus()
        self.num = 0

    # генерация бонуса
    def random_bonus(self):
        self.x = random.randint(0, DATA.block_count_width - 1)
        self.y = random.randint(0, DATA.block_count_hight - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

    # рисуем бонус
    def draw_bonus(self):
        bonus = pygame.Rect(int(self.pos.x * DATA.block_size), int(self.pos.y * DATA.block_size), DATA.block_size,
                            DATA.block_size)
        pygame.draw.rect(DATA.window, DATA.bonus_color, bonus)
