import pygame


class Rules:
    def __init__(self):
        self.rules_text = ['Цель игры - собрать всю ягоду на поле,', 'управляя змейкой с '
                                                                     'помощью клавиш W-вверх,',
                           'A-влево, S-вниз, D-вправо или же с помощью',
                           'клавиш A, D, (относительно головы), с каждым',
                           'нажатием на которые змейка поворачивается',
                           'влево (A) или вправо (D).', '', 'В настройках игры можно изменить сложность',
                           'прохождения (возможность проходить',
                           'сквозь себя, сквозь стены, а также увеличение', 'скорости с увеличение количества ягод).']

        pygame.display.set_caption('Правила игры')
        self.size_screen = 500, 500
        self.screen = pygame.display.set_mode(self.size_screen)

    def render(self):
        font = pygame.font.Font(None, 30)
        image = pygame.image.load('backgrounds_img/background_rules.png')
        fon = pygame.transform.scale(image, (500, 500))
        self.screen.blit(fon, (0, 0))  # фон
        text_coord = 100
        for i, line in enumerate(self.rules_text):
            string_rendered = font.render(line, True, pygame.Color('white'))
            text_rect = string_rendered.get_rect()
            text_coord += 5
            text_rect.top = text_coord
            text_rect.x = 10
            text_coord += text_rect.height
            self.screen.blit(string_rendered, text_rect)
        # текст - выход с помощью Enter
        font_enter = pygame.font.Font(None, 20)
        text_rendered = font_enter.render('Нажмите Enter или Esc, чтобы вернуться', True, pygame.Color('white'))
        text_rect = text_rendered.get_rect()
        text_width, text_height = font_enter.size('Нажмите Enter или Esc, чтобы вернуться')
        text_rect.x, text_rect.y = 490 - text_width, 490 - text_height
        self.screen.blit(text_rendered, text_rect)
        pygame.display.flip()

    def running(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.set_caption('Главное меню')
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        running = False
                        pygame.display.set_caption('Главное меню')
            self.render()
