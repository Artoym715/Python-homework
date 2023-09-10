__all__ = ['Matrix']


class Matrix:
    """Класс которые на входе получает матрицу и содержит методы для:
        - сравнения,
        - сложения,
        - умножения матриц."""
    def __init__(self, matr):
        """Добавляем the matr атрибут."""
        self._matr = matr

    def get_matrix(self):
        """Геттер получаем матрицу"""
        return self._matr

    def __add__(self, other):
        """Метод для сложения матриц"""
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Error: матрицы разных размеров'
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        """Метод для умножения матриц"""
        if len(self._matr[0]) != len(other._matr):
            return f'Error: невозможно перемножить матрицы'
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        """Метод для сравнения матриц"""
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Error: матрицы разных размеров'
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        return s
