# Задача: Найдите сумму цифр трехзначного числа.

n = input("Введите трехзначное число: ")

# Извлекается первый[0] символ строки,
# преобразуется к целому.
# Аналогично второй[1] и третий[2].
a = int(n[0])
b = int(n[1])
c = int(n[2])

print("Сумма цифр числа:", a + b + c)