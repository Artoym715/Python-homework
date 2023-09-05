from classes.Person import Person


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, name, surname, patronymic, age, id):
        super().__init__(name, surname, patronymic, age)
        self.id = id

    def get_level(self):
        return sum(int(num) for num in str(self.id)) % self.MAX_LEVEL
