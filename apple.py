import pygame


class SpritesClassic(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = size
        # спрайты змейки
        self.snakes_head = pygame.image.load('sprites/snakes_head.png')
        self.snakes_body = pygame.image.load('sprites/snakes_body.png')

        self.image = pygame.image.load('sprites/blueberry.png')

    def changed_image(self):
        new_size_fruit = pygame.transform.scale(self.image, (int(self.size * 2), int(self.size * 2)))
        return new_size_fruit

    def snakes_parts_h(self):
        new_snakes = pygame.transform.scale(self.snakes_head, (int(self.size * 2), int(self.size * 2)))
        return new_snakes

    def snakes_parts_b(self):
        new_snakes = pygame.transform.scale(self.snakes_body, (int(self.size * 2), int(self.size * 2)))
        return new_snakes
