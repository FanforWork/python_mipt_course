import pygame

pygame.init()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("pictures/font.ttf", size)


class DATA():
    # это наш экран, на котором отображается игра и его размеры в пикселях
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")
    # тут подгружаем картинку меню и задний фон для уровней
    BG = pygame.image.load("pictures/Background.png")
    DG = pygame.image.load("pictures/menushka.png")

    # всё игровое поле сплошное но мы его разбиваем на квадратики
    # тут у нас собственно размер такого квадратика
    block_size = 40

    # это количество квадратиков по вертикали
    block_count_hight = 18
    # это количество таких квадратиков по горизонтали
    block_count_width = 32

    game_font_size = 25

    # вспомогательное число 10 и 160
    ten = 10

    color_base = 160

    color_base0 = 80

    # screen = window
    window = pygame.display.set_mode((block_size * block_count_width, block_size * block_count_hight))
    # clock = time_count
    time_count = pygame.time.Clock()
    # цвет бонуса,змеи и война
    bonus_color = (255, 0, 0)

    warrior_color = (126, 166, 114)

    snake_color = (183, 191, 122)

    # шрифт менюшки
    menu_text_font = 100

    records_font = 20

    button_font = 75

    centr_pos_1 = 640
    # тут сразу несколько расветок окна под разные уровни
    lvl1_window = (69, 139, 0)

    lvl2_window = (85, 107, 47)

    lvl3_window = (205, 102, 0)

    lvl4_window = (224, 255, 255)

    lvl5_window = (255, 69, 0)
    #     тут количество фпс
    game_fps = 50
    # cкорость
    speedval = 240
    # цвета помогащие создать задний фон
    lvl1_back = (102, 205, 0)

    lvl2_back = (110, 139, 61)

    lvl3_back = (255, 140, 0)

    lvl4_back = (0, 255, 255)

    lvl5_back = (255, 99, 71)

    border_color = (0, 0, 0)
    # цвет счетчика
    score_color = (56, 74, 12)

    score_pos_x = 60

    score_pos_y = 700
