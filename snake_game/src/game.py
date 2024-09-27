from link import link
from link import SCREEN_UPDATE
import pygame
from data import DATA
from param import PARAMETR

pygame.init()


class GAME:
    # тут мы записываем ивенты
    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == SCREEN_UPDATE:
                link.update()
            if event.type == pygame.KEYDOWN:
                link.switch_directions(event)

    # главная функция игры
    def play_game(self):
        while True:
            link.music2()
            self.game_loop()
            if PARAMETR.parametr == 1:
                DATA.window.fill(DATA.lvl1_window)
            if PARAMETR.parametr == 2:
                DATA.window.fill(DATA.lvl2_window)
            if PARAMETR.parametr == 3:
                DATA.window.fill(DATA.lvl3_window)
            if PARAMETR.parametr == 4:
                DATA.window.fill(DATA.lvl4_window)
            if PARAMETR.parametr == 5:
                DATA.window.fill(DATA.lvl5_window)
            link.draw_elements()
            pygame.display.update()
            DATA.time_count.tick(DATA.game_fps)