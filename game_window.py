import pygame

from logics import SnakeLogics
from render import Board


class Game:
    def running(self, size=(8, 8)):
        pygame.init()
        pygame.display.set_caption('Игра')

        with open('settings.txt') as settings:
            setting = settings.read().split(';')
        game = SnakeLogics(size=size,
                           thrgh_walls=False if setting[1] == 'False' else True,
                           thrgh_self=False if setting[0] == 'False' else True,
                           control_relatively_head=False if setting[3] == 'False' else True,
                           acceleration=0 if setting[2] == 'False' else 2)
        # thrgh_walls - возможность проходить сквозь стены
        # thrgh_self - возможность проходить сквозь себя
        # acceleration - изменение скорости в процентах
        # speed - начальная скорость
        # control_relatively_head - 2 режима управления(False - глобальный; True - относительно головы)

        brd = Board(size_board=size, size_cell=50)

        run = True
        while run:
            brd.add_cells(game.body)  # game.body - массив со всеми координатами ячеек змейки
            brd.add_apple(game.apple)  # game.apple - координата яблока
            brd.render()  # Отрисовка

            for event in pygame.event.get():
                game.key_indexing(event)  # Отправляет все ивенты в класс змейки

            run = game.run
