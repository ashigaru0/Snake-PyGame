import pygame


class Rules:
    def __init__(self):
        self.rules_text = ['Правила', 'игры']  # правила и управление - недописано

        self.size_screen = 500, 500
        self.screen = pygame.display.set_mode(self.size_screen)
        pygame.display.set_caption('Правила')

    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 30)
        self.screen.fill((0, 0, 0))
        text_coord = 500 // 2 - 80
        for i, line in enumerate(self.rules_text):
            string_rendered = font.render(line, True, pygame.Color('white'))
            text_rect = string_rendered.get_rect()
            text_coord += 5
            text_rect.top = text_coord
            text_rect.x = 30
            text_coord += text_rect.height
            self.screen.blit(string_rendered, text_rect)
        pygame.display.flip()

    def running(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.display.set_caption('Главное меню')
            self.render()
