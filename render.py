import pygame


class board:
    def __init__(self, size_board=(8, 8), size_cell=100):
        self.size_cell = size_cell
        self.size_screen = (self.size_cell * size_board[0], self.size_cell * size_board[1])
        self.size_board = size_board

        self.screen = pygame.display.set_mode(self.size_screen)
        self.board = []

    def add_apple(self, apple):
        if apple:
            self.board[apple[1]][apple[0]] = 3

    def add_cells(self, cells):
        self.board = [[0] * self.size_board[0] for _ in range(self.size_board[1])]
        for num, cell in enumerate(cells):
            if num == len(cells) - 1:
                self.board[cell[1]][cell[0]] = 2
            else:
                self.board[cell[1]][cell[0]] = 1

    def render(self):
        self.screen.fill((0, 0, 0))
        for w in range(self.size_board[0]):
            for h in range(self.size_board[1]):
                x, y = w * (self.size_screen[0] // self.size_board[0]) + self.size_cell // 2, \
                       h * (self.size_screen[1] // self.size_board[1]) + self.size_cell // 2

                if self.board[h][w] == 1:
                    pygame.draw.circle(self.screen, (255, 255, 255), (x, y), self.size_cell // 2)
                elif self.board[h][w] == 2:
                    pygame.draw.circle(self.screen, (0, 255, 0), (x, y), self.size_cell // 2)
                elif self.board[h][w] == 3:
                    pygame.draw.circle(self.screen, (255, 0, 0), (x, y), self.size_cell // 2)

        pygame.display.flip()