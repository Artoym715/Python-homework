import random as rnd

__all__ = ["ChessGame"]


class ChessGame:
    """Шахматные игры"""
    _QUEEN_COUNT: int = 8  # максимальное кол-во ферзей
    _SIZE_BOARD: int = 8  # размер доски
    _TRUE_COUNT_POS = range(1, 11)  # допустимый диапазон количества генерируемых позиций

    def __init__(self):
        self._true_positions = []  # позиции с правильной расстановкой

    def check_queen(self, positions: list[tuple]) -> bool:
        """Проверка задачи о ферзях.

        :positions: позиции ферзей - кортежи (строка, столбец)
        """
        result = True

        if len(positions) != self._QUEEN_COUNT:
            result = False
        else:
            for i in range(self._QUEEN_COUNT - 1):  # берем ферзей по списку, исключая последнего
                if not result:
                    break
                row_1, col_1 = positions[i]
                for j in range(i + 1, self._QUEEN_COUNT):  # проверяем со следующими до конца списка
                    row_2, col_2 = positions[j]
                    # Ферзи на одной линии, если координаты строки или столбца у них равны.
                    # Ферзи на одной диагонали, если позицию второго можно получить из позиции первого смещением
                    # на равное количество строк и столбцов в любую из сторон
                    if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                        result = False
                        break

        return result

    def gen_true_positions(self, count_pos: int) -> list:
        """Возвращает список из заданного количества верных позиций

        :count_pos: Количество требуемых позиций _TRUE_COUNT_POS, если вне диапазона - берет минимально возможный
        """
        if count_pos not in self._TRUE_COUNT_POS:
            count_pos = min(self._TRUE_COUNT_POS)

        case_ok = 0  # удачных расстановок из всего сгенерированных
        while case_ok < count_pos:
            generated_position = self._gen_positions()
            if self.check_queen(generated_position):
                case_ok += 1
                self._true_positions.append(generated_position)

        return self._true_positions

    def _gen_positions(self) -> list[tuple[int, int]]:
        """Генератор позиций ферзей. Генерирует _QUEEN_COUNT позиций, по одному ферзю на строку.
        Для доски размером _SIZE_BOARD
        """
        result = []
        for i in range(self._SIZE_BOARD):
            result.append((i, rnd.randint(0, self._SIZE_BOARD - 1)))
        return result