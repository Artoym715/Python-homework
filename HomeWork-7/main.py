# Задача:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

string = input("Введите стихотворение Винни-Пуха ")


def rytm(str):
    count = 0
    list1 = []
    for i in range(len(str)):
        if str[i] in 'аеёиоуыэюя':
            count += 1
        if str[i] == ' ' or i == len(str) - 1:
            list1.append(count)
            count = 0
    if len(set(list1)) == 1:
        return print('Парам пам-пам')
    return print('Пам парам')


rytm(string)

# Задача: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

line, column = (map(int, input("Введите строку и столбец через пробел: ").split()))


def print_operation_table(operation, num_rows, num_columns):
    list1 = [[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1)]
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            print("{:4d}".format(list1[i][j]), end="")
        print()


print_operation_table(lambda x, y: x * y, line, column)

