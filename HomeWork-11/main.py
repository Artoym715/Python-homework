
# Задача: Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

# список для обработки
WORKING_LIST_1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# обработка списка
def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))

print(f"{WORKING_LIST_1} - {double_items(WORKING_LIST_1)}")


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

# Задача: Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

