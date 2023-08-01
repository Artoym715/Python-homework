# Задача: Напишите функцию для транспонирования матрицы

def matrixTranspose(theMatrix):
    return [*zip(*theMatrix)]

# theMatrix = [['a','b','c'],['d','e','f'],['g','h','i']]
theMatrix = [[1, 2],[3, 4]]

print(f"Начальная матрица - {theMatrix}")
print(f"Конечная матрица - {matrixTranspose(theMatrix)}")

# Задача: Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — хэш значения переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def convert_dict(dictionary) -> dict:
    return {x: v for v, x in dictionary.items()}

dictionary = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}

print("Начальный словарь: ")
for key, value in dictionary.items():
        print(f"{key}: {value}")

new_dict = convert_dict(dictionary)

print("Конечный словарь: ")
for key, value in new_dict.items():
        print(f"{key}: {hash(value)}")