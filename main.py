import pygame

from logics import snake_logics
from render import board  # Вот это нужно переписать


if __name__ == '__main__':
    pygame.init()
    size = (8, 12)

    game = snake_logics(size=size, thrgh_walls=False, thrgh_self=False)
    # thrgh_walls - возможность проходить сквозь стены
    # thrgh_self - возможность проходить сквозь себя
    # acceleration - изменение скорости в процентах
    # speed - начальная скорость
    # control_relatively_head - 2 режима управления(0 - глобальный; 1 - относительно головы)

    brd = board(size_board=size, size_cell=50)

    run = True
    while run:
        brd.add_cells(game.body)      # game.body - массив со всеми координатами ячеек змейки
        brd.add_apple(game.apple)     # game.apple - координата яблока
        brd.render()                  # Отрисовка

        for event in pygame.event.get():
            game.key_indexing(event)  # Отправляет все ивенты в класс змейки

        run = game.run


