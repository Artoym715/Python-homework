from random import randint
import itertools
import copy
# Задача: Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

# список для обработки
WORKING_LIST_1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# обработка списка
def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))

print(f"{WORKING_LIST_1} - {double_items(WORKING_LIST_1)}")
print()

# Задача: В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

# Текст для обработки ресурс https://www.blindtextgenerator.com/lorem-ipsum
WORK_TEXT ="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
           "Aenean commodo ligula eget dolor. Aenean massa. " \
           "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. " \
           "Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. " \
           "Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. " \
           "Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. " \
           "Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. " \
           "Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. " \
           "Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. " \
           "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. " \
           "Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. " \
           "Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. " \
           "Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"

# кол-во требуемых слов
FREQUENT_COUNT = 10


# Возврат count_words самых часто используемых слов из текста в виде строки, разделенных пробелами
def most_frequent_words(text: str, count_words: int) -> dict:
    # удалить знаки препинания, привести к единому регистру, тире ищем только как знак препинания,
    # дефис разделяющий части слова - является его частью
    words_list = text.upper() \
        .replace(".", " ") \
        .replace(",", " ") \
        .replace(";", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("?", " ") \
        .replace(" - ", " ") \
        .split()
    # подсчитываем кол-во слов, используем словарь для этого
    words_count = {}
    for w in words_list:
        words_count[w] = words_list.count(w)
    # сортируем словарь по значениям, отбираем только нужное количество
    return dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:count_words])

for i, w in enumerate(most_frequent_words(WORK_TEXT, FREQUENT_COUNT).items(), 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")
print()
# Задача: Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

# Словарь вещей
THINGS_DICT = {"вилка": 1,
               "ложка": 1,
               "вода": 3,
               "ботинки": 3,
               "куртка": 5,
               "камера": 4,
               "чайник": 4,
               "палатка": 12,
               "еда": 5,
               "джинсы": 4,
               "посуда": 2,
               }
# Размер рюкзака
BAG_SIZE = 5


def bag_pack(things: dict[str, int], bag_volume: int, mode_greed=True) -> list[int | set]:
    """'Жадный' или 'Щедрый' рюкзак - забирает вещи пока есть место.
    В жадном режиме заполняет начиная с вещей от большего веса к меньшему,
    в щедром - наоборот, заполнение ведется от вещей с наименьшим весом.

    :things: словарь вещей для анализа
    :bag_volume: размер заполняемого рюкзака
    :mode_greed: режим работы True - жадный, False - щедрый
    """
    tmp_dict = dict(sorted(things.items(), key=lambda x: x[1], reverse=mode_greed))
    things_list: [int | set] = [0, set()]  # первый элемент - занятый размер, остальное - уложенные вещи
    # пока не наполнен рюкзак
    for t_key, t_val in tmp_dict.items():
        if (things_list[0] + t_val) <= bag_volume:
            things_list[1].add(t_key)
            things_list[0] += t_val

    return things_list


def bag_all_pack(things: dict[str, int], bag_volume: int) -> list:
    """Поиск всех вариантов упаковки.

    :things: словарь вещей для анализа
    :bag_volume: размер заполняемого рюкзака
    """
    bag_list: list[list[int | set]] = []
    best_case = 0
    # отобрать только подходящие вещи
    for t_key, t_val in things.items():
        # пропустить - если вещь не влазит в рюкзак
        if t_val <= BAG_SIZE:
            tmp_list = []
            for x in bag_list:
                # пропустить, если добавление невозможно к существующему набору
                weight = x[0] + t_val
                if bag_volume >= weight and not x[1].issubset(t_key):
                    y: list[int | set] = copy.deepcopy(x)
                    y[0] += t_val
                    y[1].add(t_key)
                    tmp_list.append(y)
                    if weight > best_case:
                        best_case = weight
            if len(tmp_list):
                for t in tmp_list:
                    bag_list.append(t)
            if bag_volume >= t_val:
                bag_list.append([t_val, {t_key}])
                if t_val > best_case:
                    best_case = t_val

    bag_list = list(filter(lambda b: b[0] == best_case, bag_list))
    return bag_list


def print_bag(bag: list[int | set]):
    """Вывод содержимого рюкзака."""
    for x in bag:
        if isinstance(x, int):
            print(f"Взято {x}", end=" | ")
        else:
            print(f"{x}")

print(f"Размер рюкзака - {BAG_SIZE}")
print("Перечень вещей:")
print(THINGS_DICT)
print()
print("Жадный алгоритм:")
print_bag(bag_pack(THINGS_DICT, BAG_SIZE))
print()
print("Щедрый алгоритм:")
print_bag(bag_pack(THINGS_DICT, BAG_SIZE, False))
print()
print("Все наилучшие варианты:")
for x in bag_all_pack(THINGS_DICT, BAG_SIZE):
    print_bag(x)
print()
# Доп Задача: Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 10) многочлена и записать как многочлен степени k.
# Пример:
#  k=2  - это максимальная степень многочлена, то есть в данном случае будет x2
#  - > 2*x² + 4*x + 5 = 0  при списке [2 ,4 ,5 ]
#        или  x² + 5 = 0   при списке [1 ,0 ,5 ]
#        или  10*x² = 0   при списке [10 ,0 ,0 ]
# k=3 - > 5*x^3 + 6*x^2 + 7*x + 10 = 0 при списке [ 5 , 6 , 7, 10]

k = int(input('Задайте натуральную степень k: '))
ratio_list = list([randint(0, 11) for i in range(k+1)]) # задаем случайный список
if ratio_list[0] == 0: # если будет равен 0, то многочлен может быть неверным
    ratio_list[0] = randint(1, 11)
print(ratio_list)

def get_polynomial(k, ratio_list): # далее идет загугливание информации
    str1 = ['*x**']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    # с помощью этого метода мы объединяем несколько списков в список кортежей с самой длинной итерацией
    # пустые кортежи заполняем пустотой ('')
    # print(polynomial)
    for x in polynomial:
        x.append(' + ') # проставляем + между кортежами
    polynomial = list(itertools.chain(*polynomial)) # объединяем в один список
    # print(polynomial)
    polynomial[-1] = ' = 0' # добавляем в конец (меняем последний '+' на '= 0')
    return "".join(map(str, polynomial)).replace(' 1*x',' x') # возвращаем строку

list = get_polynomial(k, ratio_list)
print(list)

