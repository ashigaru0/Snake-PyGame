import pygame

import sys

from rules_window import Rules
from game_window import Game
from settings_window import Settings


class MainMenu:
    def __init__(self):
        self.menu_text = ['Начать игру', 'Правила', 'Настройки', 'Выход', 'Рекорд:', 0]
        self.text_index = 0

        pygame.display.set_caption('Главное меню')
        self.size_screen = 500, 500
        self.screen = pygame.display.set_mode(self.size_screen)

    def check_menu_text(self, direction):
        self.text_index += 0 if (self.text_index == 0 and direction == -1) or \
                                (self.text_index == 3 and direction == 1) else direction

    def open_windows(self):
        if self.text_index == 0:
            Game().running()
        elif self.text_index == 1:
            Rules().running()
        elif self.text_index == 2:
            Settings().running()
        else:
            pygame.quit()
            sys.exit()

    def render(self):
        with open('record.txt', mode='r') as rec:
            self.menu_text[-1] = rec.read()

        image = pygame.image.load('backgrounds_img/background_menu.png')
        fon = pygame.transform.scale(image, (500, 500))
        self.screen.blit(fon, (0, 0))  # фон
        font = pygame.font.Font(None, 40)
        text_coord = 180
        for i, line in enumerate(self.menu_text):
            string_rendered = font.render(line, True, pygame.Color('white'))
            text_rect = string_rendered.get_rect()
            text_coord += 20
            text_rect.top = text_coord
            text_rect.x = 20
            text_coord += text_rect.height
            if i == self.text_index:
                pygame.draw.rect(self.screen, (61, 0, 153), text_rect)
            self.screen.blit(string_rendered, text_rect)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main_menu = MainMenu()

    running = True
    while running:
        main_menu.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    main_menu.check_menu_text(-1)  # выбор опции, наверх
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    main_menu.check_menu_text(1)  # выбор опции, вниз
                elif event.key == pygame.K_RETURN:
                    main_menu.open_windows()  # переход

    pygame.quit()
