# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип экземпляра (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.

from factory.Factory import Factory
from chess.Chess import ChessGame

factory = Factory()

games = ChessGame()


employee = factory.create_employee("employee", "Дмитрий", "Бурычин", "Сергеевич", 29, 57889)
fish = factory.create_animal("fish", 10, 20, True, "Окунь")

print(employee.get_level())
fish.move()
print(fish.get_species())
print(games.gen_true_positions(2))


