# Задача: Найдите сумму цифр трехзначного числа.

n = input("Введите трехзначное число: ")

# Извлекается первый[0] символ строки,
# преобразуется к целому.
# Аналогично второй[1] и третий[2].
a = int(n[0])
b = int(n[1])
c = int(n[2])

print("Сумма цифр числа:", a + b + c)

# Задача: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input("Введите общее кол-во Журавликов сделанных  Петей, Катей и Сережой: "))
sergey = s / 6
petr = sergey
ekaterina = (sergey + petr) * 2
print('Сережа сделал: {} журавликов'.format(int(sergey)))
print('Катя сделала: {} журавликов'.format(int(ekaterina)))
print('Петя сделал: {} журавликов'.format(int(petr)))