import pygame, sys, shelve
from button import BUTTON
from data import DATA
from data import get_font
from param import PARAMETR


class MENU:

    def __init__(self):
        self.sound1 = pygame.mixer.Sound('sounds/menushka.mp3')

    def music1(self):
        self.sound1.play()

    def stop_music(self):
        self.sound1.stop()

    def change_param1(self):
        PARAMETR.parametr = 1

    def change_param2(self):
        PARAMETR.parametr = 2

    def change_param3(self):
        PARAMETR.parametr = 3

    def change_param4(self):
        PARAMETR.parametr = 4

    def change_param5(self):
        PARAMETR.parametr = 5

    def ChooseLevel(self):
        level_chosen = False
        while not level_chosen:
            DATA.SCREEN.blit(DATA.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(DATA.menu_text_font).render("LEVELS", True, "#b60f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(DATA.centr_pos_1, DATA.menu_text_font))

            LVL1 = BUTTON(image=pygame.image.load("pictures/Play Rect.png"),
                          pos=(4 * DATA.menu_text_font, 2.5 * DATA.menu_text_font),
                          text_input="LVL1", font=get_font(DATA.button_font), base_color="#d7fcd4",
                          hovering_color="Green")
            LVL2 = BUTTON(image=pygame.image.load("pictures/Play Rect.png"),
                          pos=(4 * DATA.menu_text_font, 4 * DATA.menu_text_font),
                          text_input="LVL2", font=get_font(DATA.button_font), base_color="#d7fcd4",
                          hovering_color="Green")
            LVL3 = BUTTON(image=pygame.image.load("pictures/Play Rect.png"),
                          pos=(4 * DATA.menu_text_font, 5.5 * DATA.menu_text_font),
                          text_input="LVL3", font=get_font(DATA.button_font), base_color="#d7fcd4",
                          hovering_color="Green")
            LVL4 = BUTTON(image=pygame.image.load("pictures/Play Rect.png"),
                          pos=(9 * DATA.menu_text_font, 2.5 * DATA.menu_text_font),
                          text_input="LVL4", font=get_font(DATA.button_font), base_color="#d7fcd4",
                          hovering_color="Green")
            LVL5 = BUTTON(image=pygame.image.load("pictures/Play Rect.png"),
                          pos=(9 * DATA.menu_text_font, 4 * DATA.menu_text_font),
                          text_input="LVL5", font=get_font(DATA.button_font), base_color="#d7fcd4",
                          hovering_color="Green")

            OPTIONS_BACK = BUTTON(image=None, pos=(9 * DATA.menu_text_font, 5.5 * DATA.menu_text_font),
                                  text_input="BACK", font=get_font(DATA.button_font), base_color="Blue",
                                  hovering_color="Green")

            OPTIONS_BACK.change_color(MENU_MOUSE_POS)
            OPTIONS_BACK.update(DATA.SCREEN)

            DATA.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [LVL1, LVL2, LVL3, LVL4, LVL5]:
                button.change_color(MENU_MOUSE_POS)
                button.update(DATA.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.check_for_input(MENU_MOUSE_POS):
                        self.main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.stop_music()
                    from game import GAME
                    gam = GAME()
                    if LVL1.check_for_input(MENU_MOUSE_POS):
                        level_chosen = True
                        # self.parametr = 1
                        self.change_param1()
                        gam.play_game()
                    if LVL2.check_for_input(MENU_MOUSE_POS):
                        level_chosen = True
                        # self.parametr = 2
                        self.change_param2()
                        gam.play_game()
                    if LVL3.check_for_input(MENU_MOUSE_POS):
                        level_chosen = True
                        # self.parametr = 3
                        self.change_param3()
                        gam.play_game()
                    if LVL4.check_for_input(MENU_MOUSE_POS):
                        level_chosen = True
                        # self.parametr = 4
                        self.change_param4()
                        gam.play_game()
                    if LVL5.check_for_input(MENU_MOUSE_POS):
                        level_chosen = True
                        # self.parametr = 5
                        self.change_param5()
                        gam.play_game()

            pygame.display.update()

    def play(self):
        self.ChooseLevel()

    # пишем таблицу рекордов
    def records(self):
        d1 = shelve.open('score1.db')  # open the shelve file
        if d1:  # check if the 'high_score' key exists in the shelve file
            high_score = max(d1.values())  # retrieve the high score
        else:
            high_score = 0  # if 'high_score' key does not exist, initialize it to 0
        max1 = "LVL1 Record: " + str(high_score)
        d1.close()

        d2 = shelve.open('score2.db')  # open the shelve file
        if 'high_score' in d2:  # check if the 'high_score' key exists in the shelve file
            high_score = d2['high_score']  # retrieve the high score
        else:
            high_score = 0  # if 'high_score' key does not exist, initialize it to 0
        max2 = "LVL2 Record: " + str(high_score)
        d2.close()

        d3 = shelve.open('score3.db')  # open the shelve file
        if 'high_score' in d3:  # check if the 'high_score' key exists in the shelve file
            high_score = d3['high_score']  # retrieve the high score
        else:
            high_score = 0  # if 'high_score' key does not exist, initialize it to 0
        max3 = "LVL3 Record: " + str(high_score)
        d3.close()

        d4 = shelve.open('score4.db')  # open the shelve file
        if 'high_score' in d4:  # check if the 'high_score' key exists in the shelve file
            high_score = d4['high_score']  # retrieve the high score
        else:
            high_score = 0  # if 'high_score' key does not exist, initialize it to 0
        max4 = "LVL4 Record: " + str(high_score)
        d4.close()

        d5 = shelve.open('score5.db')  # open the shelve file
        if 'high_score' in d5:  # check if the 'high_score' key exists in the shelve file
            high_score = d5['high_score']  # retrieve the high score
        else:
            high_score = 0  # if 'high_score' key does not exist, initialize it to 0
        max5 = "LVL5 Record: " + str(high_score)
        d5.close()
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            DATA.SCREEN.fill("white")

            OPTIONS_TEXT1 = get_font(DATA.records_font).render(max1, True, "Black")
            OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(DATA.centr_pos_1, 0.5 * DATA.menu_text_font))
            DATA.SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)

            OPTIONS_TEXT2 = get_font(DATA.records_font).render(max2, True, "Black")
            OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(DATA.centr_pos_1, DATA.menu_text_font))
            DATA.SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

            OPTIONS_TEXT3 = get_font(DATA.records_font).render(max3, True, "Black")
            OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(DATA.centr_pos_1, 1.5 * DATA.menu_text_font))
            DATA.SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

            OPTIONS_TEXT4 = get_font(DATA.records_font).render(max4, True, "Black")
            OPTIONS_RECT4 = OPTIONS_TEXT4.get_rect(center=(DATA.centr_pos_1, 2 * DATA.menu_text_font))
            DATA.SCREEN.blit(OPTIONS_TEXT4, OPTIONS_RECT4)

            OPTIONS_TEXT5 = get_font(DATA.records_font).render(max5, True, "Black")
            OPTIONS_RECT5 = OPTIONS_TEXT5.get_rect(center=(DATA.centr_pos_1, 2.5 * DATA.menu_text_font))
            DATA.SCREEN.blit(OPTIONS_TEXT5, OPTIONS_RECT5)

            OPTIONS_BACK = BUTTON(image=None, pos=(DATA.centr_pos_1, 4.6 * DATA.menu_text_font),
                                  text_input="BACK", font=get_font(DATA.button_font), base_color="Black",
                                  hovering_color="Green")

            OPTIONS_BACK.change_color(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(DATA.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.check_for_input(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    # менюшка
    def main_menu(self):
        while True:
            DATA.SCREEN.blit(DATA.DG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(DATA.menu_text_font).render("MAIN MENU", True, "#006400")
            MENU_RECT = MENU_TEXT.get_rect(center=(DATA.centr_pos_1, DATA.menu_text_font))

            PLAY_BUTTON = BUTTON(image=pygame.image.load("pictures/Play Rect.png"),
                                 pos=(DATA.centr_pos_1, 2.5 * DATA.menu_text_font),
                                 text_input="PLAY", font=get_font(DATA.button_font), base_color="#d7fcd4",
                                 hovering_color="Black")
            OPTIONS_BUTTON = BUTTON(image=pygame.image.load("pictures/Options Rect.png"),
                                    pos=(DATA.centr_pos_1, 4 * DATA.menu_text_font),
                                    text_input="RECORDS", font=get_font(DATA.button_font), base_color="#d7fcd4",
                                    hovering_color="Black")
            QUIT_BUTTON = BUTTON(image=pygame.image.load("pictures/Quit Rect.png"),
                                 pos=(DATA.centr_pos_1, 5.5 * DATA.menu_text_font),
                                 text_input="QUIT", font=get_font(DATA.button_font), base_color="#d7fcd4",
                                 hovering_color="Black")

            DATA.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.change_color(MENU_MOUSE_POS)
                button.update(DATA.SCREEN)

            self.music1()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                        self.play()
                    if OPTIONS_BUTTON.check_for_input(MENU_MOUSE_POS):
                        self.records()
                    if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


menu_instance = MENU()
menu_instance.main_menu()
