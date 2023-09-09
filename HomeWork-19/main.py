# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# умножения матриц
# Добавить документации к классу и методам класса.
# Добавить обработку некорректных значений.

from matrix_class.Matrix import Matrix

m_1 = [
    [1, 2, 4],
    [5, 6,  8],
    [2, 5, -2],
    [10, 5, 0]
]

m_2 = [
    [1, 2, 4],
    [5, 6,  8],
    [5, 6,  8],
    [-2, 2, 0]
]

m_3 = [
    [1, 2, 4, 5],
    [5, 6, 8, 0],
    [5, 0, -7, 1]
]

m_4 = [
      [1, 2, 4, 5, 0],
      [5, 6, 8, 0, 0],
      [5, 0, -7, 1, 0]
]

matr_1 = Matrix(m_1)
matr_2 = Matrix(m_2)
matr_3 = Matrix(m_3)
matr_4 = Matrix(m_4)

print ("Cложение матриц:")
matr_sum = matr_1 + matr_2
print(matr_sum)

print ("Умножение матриц:")
matr_mul = matr_1 * matr_3
print(matr_mul)
print(matr_1 * matr_4)

print ("Cравнение матриц:")
print(matr_1 == matr_1)
print(matr_1 == matr_2)