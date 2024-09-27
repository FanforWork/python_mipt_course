import pygame
from data import DATA


# класс отвечяет за змейку
class SNAKE:
    def __init__(self):
        self.body = [pygame.math.Vector2(5, DATA.ten), pygame.math.Vector2(6, DATA.ten),
                     pygame.math.Vector2(7, DATA.ten)]
        self.direction = pygame.math.Vector2(-1, 0)
        # new_block = new_tail
        self.new_tail = False

    # тут змейка рисуется
    def draw_snake(self):
        for block in self.body:
            # block_rect = zmey_block
            x_axis = int(block.x * DATA.block_size)
            y_axis = int(block.y * DATA.block_size)
            zmey_block = pygame.Rect(x_axis, y_axis, DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.snake_color, zmey_block)

    #  тут змей перемещается
    def move_snake(self):
        if self.new_tail == True:
            body_copy = self.body[:]
            self.new_tail = False
        else:
            body_copy = self.body[:-1]
        # body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    # увеличение змея на блок
    def grow(self):
        self.new_tail = True
