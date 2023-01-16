import pygame
from checkbox import Checkbox


class Settings:
    def __init__(self):
        self.size_screen = 500, 500
        self.screen = pygame.display.set_mode(self.size_screen)
        self.rules_text = [('Настройки', 75, (10, 10)),
                           ('Проход сквозь себя:', 36, (10, 70), Checkbox(self.screen, 430, 77, 1)),
                           ('Проход сквозь стены:', 36, (10, 110), Checkbox(self.screen, 430, 117, 2)),
                           ('Увелечение скорости:', 36, (10, 150), Checkbox(self.screen, 430, 157, 3)),
                           ('Контроль относительно головы:', 36, (10, 190), Checkbox(self.screen, 430, 197, 4))]
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
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, self.rules_text[0][1])
        text = font.render(self.rules_text[0][0], True,
                           (255, 255, 255)) # 129, 64, 175
        pygame.draw.rect(self.screen, (61, 0, 153), self.rules_text[0][2] + (270, 50))
        self.screen.blit(text, self.rules_text[0][2])
        for line in self.rules_text[1::]:
            font = pygame.font.Font(None, line[1])
            text = font.render(line[0], True,
                               (255, 255, 255))
            self.screen.blit(text, line[2])
            line[3].render_checkbox()
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
                    if event.key == pygame.K_ESCAPE:
                        self.save_settings()
                        running = False
                        pygame.display.set_caption('Главное меню')
                for line in self.rules_text[1::]:
                    line[3].update_checkbox(event)
            self.render()
