__all__ = ["Person"]


class Person:
    def __init__(self, name, surname, patronymic, age):
       self.name = name
       self.surname = surname
       self.patronymic = patronymic
       self._age = age

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"