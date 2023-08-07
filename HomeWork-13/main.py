import os
# Задача: Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

full_puth = __file__

def info_file(full_path):
    path_file = os.getcwd()
    full_name = full_path.split("/")[-1].split(".")
    name_file, expansion_file = full_name[0], "." + full_name[1]
    info = (path_file, name_file, expansion_file)
    return info

print(info_file(full_puth))
print()
# Задача: Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Петя', 'Маша', 'Саша']
bets = [35_000, 40_000, 300_000]
prizes = ['23%', '32.5%', '100%']

def dict_summ_prize_and_bet(list_name, list_bet, list_prize):
    dict_func = {}
    for name_key, bet, prize in zip(list_name, list_bet, list_prize):
        dict_func[name_key] = bet + ((bet / 100) * (float(prize.replace("%",""))))
    return dict_func


dict_generator = {name_key: bet + ((bet / 100) * (float(prize.replace("%","")))) for name_key, bet, prize in zip(names, bets, prizes)}
for key, values in dict_generator.items():
    print(f"Имя сотрудника: {key} \t зарплата сотрудника с учётом премии: {values} ")
# Задача: Создайте функцию генератор чисел Фибоначчи (см. Википедию).