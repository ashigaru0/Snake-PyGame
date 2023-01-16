import pygame
from checkbox import Checkbox


class Settings:
    def __init__(self):
        self.size_screen = 500, 500
        self.screen = pygame.display.set_mode(self.size_screen)
        self.rules_text = [('Настройки', 75, (10, 10)),
                           ('Проход сквозь себя:', 36, (10, 70), Checkbox(self.screen, 430, 77, 1)),
                           ('Проход сквозь стены:', 36, (10, 100), Checkbox(self.screen, 430, 107, 2)),
                           ('Увелечение скорости:', 36, (10, 130), Checkbox(self.screen, 430, 137, 3)),
                           ('Контроль относительно головы:', 36, (10, 160), Checkbox(self.screen, 430, 167, 4))]
        self.load_settings()

        pygame.display.set_caption('Настройки')

    def load_settings(self):
        with open('settings.txt', mode='r') as settings:
            setting = settings.read().split(';')
            if setting:
                for indx, line in enumerate(self.rules_text[1::]):
                    self.rules_text[indx + 1][3].checked = False if setting[indx] == 'False' else True

    def save_settings(self):
        with open('settings.txt', mode='w') as settings:
            for line in self.rules_text[1::]:
                settings.write(f'{line[3].checked};')

    def render(self):
        image = pygame.image.load('backgrounds_img/background_settings.png')
        fon = pygame.transform.scale(image, (500, 500))
        self.screen.blit(fon, (0, 0))  # фон
        for indx, line in enumerate(self.rules_text):
            font = pygame.font.Font(None, line[1])
            text = font.render(line[0], True,
                               (255, 255, 255))
            self.screen.blit(text, line[2])
            if indx != 0:
                line[3].render_checkbox()
        # текст - выход с помощью Enter
        font_enter = pygame.font.Font(None, 20)
        text_rendered = font_enter.render('Нажмите Enter, чтобы вернуться', True, pygame.Color('white'))
        text_rect = text_rendered.get_rect()
        text_width, text_height = font_enter.size('Нажмите Enter, чтобы вернуться')
        text_rect.x, text_rect.y = 490 - text_width, 490 - text_height
        self.screen.blit(text_rendered, text_rect)

        pygame.display.flip()

    def running(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_settings()
                    running = False
                    pygame.display.set_caption('Настройки')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.save_settings()
                        running = False
                        pygame.display.set_caption('Главное меню')
                for line in self.rules_text[1::]:
                    line[3].update_checkbox(event)
            self.render()
