__all__ = ['TestName']


class NameExeption(Exception):
    pass


class NameErorr(NameExeption):

    def __str__(self):
        return f'Неверные данные для ФИО!'


class TestName:
    """Проверка правильности ввода ФИО. Имена должны быть только буквами и начинаться с заглавных."""

    def __set_name__(self, owner, name):
        """Установить имя проверяемого атрибута."""
        self.param_name = name

    def __get__(self, instance, owner):
        """Вернуть значение атрибута."""
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value: str):
        """Установить значение атрибута."""
        if not value.isalpha() or not value.istitle():
            raise NameErorr
        instance.__dict__[self.param_name] = value
