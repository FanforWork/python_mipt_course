import pygame
import shelve
from snake import SNAKE
from bonus import BONUS
from warrior import WARRIOR
from data import DATA
from param import PARAMETR

pygame.init()
game_font = pygame.font.Font(None, DATA.game_font_size)


class LINK:
    def __init__(self):
        self.snake = SNAKE()
        self.warrior = WARRIOR()
        self.speed = DATA.speedval
        self.bonus = BONUS()
        self.sound2 = pygame.mixer.Sound('sounds/Broken Vessel.mp3')

    def music2(self):
        self.sound2.play()

    def update(self):
        self.snake.move_snake()
        self.ukus()
        self.uron_zmey()
        if len(self.snake.body) % DATA.ten == 0:
            self.bonus_catch()

    def draw_elements(self):
        self.background()
        self.warrior.draw_warrior()
        self.score()
        self.snake.draw_snake()
        if len(self.snake.body) % DATA.ten == 0:
            self.bonus.draw_bonus()

    # check_collision = ukus
    def ukus(self):
        if self.warrior.pos == self.snake.body[0]:
            self.warrior.randomize(PARAMETR.parametr)
            self.snake.grow()
            self.speed *= 0.99
            pygame.time.set_timer(SCREEN_UPDATE, int(link.speed))

    def bonus_catch(self):
        if self.bonus.pos == self.snake.body[0]:
            self.bonus.random_bonus()
            self.bonus.num += 9
            self.snake.grow()
            self.speed *= 1
            pygame.time.set_timer(SCREEN_UPDATE, int(link.speed))

    # рисуем задний фон в зависимости от уровня
    @staticmethod
    def background():
        if PARAMETR.parametr == 1:
            back_color = DATA.lvl1_back
        if PARAMETR.parametr == 2:
            back_color = DATA.lvl2_back
        if PARAMETR.parametr == 3:
            back_color = DATA.lvl3_back
        if PARAMETR.parametr == 4:
            back_color = DATA.lvl4_back
        if PARAMETR.parametr == 5:
            back_color = DATA.lvl5_back

        link.drawer(back_color)
        if PARAMETR.parametr == 2:
            link.lvl2_draw()
        if PARAMETR.parametr == 3:
            link.lvl3_draw()
        if PARAMETR.parametr == 4:
            link.lvl4_draw()
        if PARAMETR.parametr == 5:
            link.lvl5_draw()

    @staticmethod
    def drawer(back_color):
        for colum in range(DATA.block_count_width):
            if colum % 2 == 0:
                for raw in range(DATA.block_count_hight):
                    if raw % 2 == 0:
                        block_color = pygame.Rect(colum * DATA.block_size, raw * DATA.block_size, DATA.block_size,
                                                  DATA.block_size)
                        pygame.draw.rect(DATA.window, back_color, block_color)
            else:
                for raw in range(DATA.block_count_hight):
                    if raw % 2 != 0:
                        block_color = pygame.Rect(colum * DATA.block_size, raw * DATA.block_size, DATA.block_size,
                                                  DATA.block_size)
                        pygame.draw.rect(DATA.window, back_color, block_color)

    @staticmethod
    def lvl2_draw():
        for raw in range(int(DATA.block_count_hight / 3)):
            block_color = pygame.Rect(2 * DATA.color_base, DATA.color_base0 + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for raw in range(int(DATA.block_count_hight / 2)):
            block_color = pygame.Rect(9 * DATA.color_base0, 9 * DATA.block_size + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)

    @staticmethod
    def lvl3_draw():
        for raw in range(int(DATA.block_count_hight / 2)):
            block_color = pygame.Rect(5 * DATA.color_base0, DATA.color_base + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for raw in range(int(DATA.block_count_hight / 2)):
            block_color = pygame.Rect(5.5 * DATA.color_base, DATA.color_base + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for raw in range(int(DATA.block_count_hight / 2)):
            block_color = pygame.Rect(8 * DATA.color_base0, DATA.color_base + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)

    @staticmethod
    def lvl4_draw():
        for raw in range(int(DATA.block_count_hight - 2)):
            block_color = pygame.Rect(2 * DATA.color_base, DATA.color_base0 + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for raw in range(int(DATA.block_count_hight - 2)):
            block_color = pygame.Rect(5.5 * DATA.color_base, raw * DATA.block_size, DATA.block_size,
                                      DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)

    @staticmethod
    def lvl5_draw():
        for raw in range(int(DATA.block_count_hight / 2 - 5)):
            block_color = pygame.Rect(2 * DATA.color_base, DATA.color_base0 + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for raw in range(int(DATA.block_count_hight / 2 - 5)):
            block_color = pygame.Rect(2 * DATA.color_base, 6 * DATA.color_base0 + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for raw in range(int(DATA.block_count_hight - 6)):
            block_color = pygame.Rect(7 * DATA.color_base, 1.5 * DATA.color_base0 + raw * DATA.block_size,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for colum in range(int(DATA.block_count_width / 2)):
            block_color = pygame.Rect(6 * DATA.color_base0 + colum * DATA.block_size, 1.5 * DATA.color_base0,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)
        for colum in range(int(DATA.block_count_width / 2)):
            block_color = pygame.Rect(6 * DATA.color_base0 + colum * DATA.block_size, 7 * DATA.color_base0,
                                      DATA.block_size, DATA.block_size)
            pygame.draw.rect(DATA.window, DATA.border_color, block_color)

    # что происходит перед смертью
    def game_over(self):
        if PARAMETR.parametr == 1:
            high_score = len(self.snake.body) + self.bonus.num - 3
            d1 = shelve.open('score1.db')
            d1['high_score'] = high_score
            d1.close()
        if PARAMETR.parametr == 2:
            high_score = len(self.snake.body) + self.bonus.num - 3
            d2 = shelve.open('score2.db')
            d2['high_score'] = high_score
            d2.close()
        if PARAMETR.parametr == 3:
            high_score = len(self.snake.body) + self.bonus.num - 3
            d3 = shelve.open('score3.db')
            d3['high_score'] = high_score
            d3.close()
        if PARAMETR.parametr == 4:
            high_score = len(self.snake.body) + self.bonus.num - 3
            d4 = shelve.open('score4.db')
            d4['high_score'] = high_score
            d4.close()
        if PARAMETR.parametr == 5:
            high_score = len(self.snake.body) + self.bonus.num - 3
            d5 = shelve.open('score5.db')
            d5['high_score'] = high_score
            d5.close()
        pygame.quit()
        exit()

    def hit_border(self):
        if not (0 <= self.snake.body[0].x < DATA.block_count_width):
            self.game_over()
        if not (0 <= self.snake.body[0].y < DATA.block_count_hight):
            self.game_over()

    # ударили препядствие на карте
    def hit_smth(self):
        if PARAMETR.parametr == 2:
            link.lvl2_hit()
        if PARAMETR.parametr == 3:
            link.lvl3_hit()
        if PARAMETR.parametr == 4:
            link.lvl4_hit()
        if PARAMETR.parametr == 5:
            link.lvl5_hit()

    def lvl2_hit(self):
        if 9 > self.snake.body[0].x >= 8 > self.snake.body[0].y >= 2:
            self.game_over()
        if 1.9 * DATA.ten > self.snake.body[0].x >= 1.8 * DATA.ten > self.snake.body[0].y >= 9:
            self.game_over()

    def lvl3_hit(self):
        if 1.1 * DATA.ten > self.snake.body[0].x >= DATA.ten and 1.3 * DATA.ten > self.snake.body[0].y >= 4:
            self.game_over()
        if 2.3 * DATA.ten > self.snake.body[0].x >= 2.2 * DATA.ten and 1.3 * DATA.ten > self.snake.body[0].y >= 4:
            self.game_over()
        if 1.7 * DATA.ten > self.snake.body[0].x >= 1.6 * DATA.ten and 1.3 * DATA.ten > self.snake.body[0].y >= 4:
            self.game_over()

    def lvl4_hit(self):
        if 2.3 * DATA.ten > self.snake.body[0].x >= 2.2 * DATA.ten and DATA.block_count_hight - 2 > self.snake.body[
            0].y >= 0:
            self.game_over()
        if 9 > self.snake.body[0].x >= 8 and DATA.block_count_hight > self.snake.body[0].y >= 2:
            self.game_over()

    def lvl5_hit(self):
        if 9 > self.snake.body[0].x >= 8 and 1.6 * DATA.ten > self.snake.body[0].y >= 1.2 * DATA.ten:
            self.game_over()
        if 9 > self.snake.body[0].x >= 8 and 6 > self.snake.body[0].y >= 2:
            self.game_over()
        if 2.9 * DATA.ten > self.snake.body[0].x >= 1.2 * DATA.ten and 4 > self.snake.body[0].y >= 3:
            self.game_over()
        if 2.9 * DATA.ten > self.snake.body[0].x >= 1.2 * DATA.ten and 1.5 * DATA.ten > self.snake.body[
            0].y >= 1.4 * DATA.ten:
            self.game_over()
        if 2.9 * DATA.ten > self.snake.body[0].x >= 2.8 * DATA.ten and 1.4 * DATA.ten > self.snake.body[0].y >= 4:
            self.game_over()

    # чекаем если змей ударился
    def uron_zmey(self):
        self.hit_border()
        self.hit_smth()
        for part in self.snake.body[1:]:
            if part == self.snake.body[0]:
                self.game_over()

    # счёт игровой
    def score(self):
        score_text = str(len(self.snake.body) + self.bonus.num - 3)
        score_surface = game_font.render(score_text, True, DATA.score_color)
        x_pos = int(DATA.block_count_width * DATA.block_size - DATA.score_pos_x)
        y_pos = int(DATA.block_count_hight * DATA.block_size - DATA.score_pos_y)
        score_block = score_surface.get_rect(center=(x_pos, y_pos))
        DATA.window.blit(score_surface, score_block)

    # изменение направления при нажатии клавиш
    @staticmethod
    def switch_directions(event):
        if event.key == pygame.K_w:
            if link.snake.direction.y != 1:
                link.snake.direction = pygame.math.Vector2(0, -1)
        if event.key == pygame.K_a:
            if link.snake.direction.x != 1:
                link.snake.direction = pygame.math.Vector2(-1, 0)
        if event.key == pygame.K_d:
            if link.snake.direction.x != -1:
                link.snake.direction = pygame.math.Vector2(1, 0)
        if event.key == pygame.K_s:
            if link.snake.direction.y != -1:
                link.snake.direction = pygame.math.Vector2(0, 1)


link = LINK()

SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, int(link.speed))
