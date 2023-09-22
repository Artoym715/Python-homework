__all__ = ['TestRate']


class RateExeption(Exception):
    pass


class RateTypeErorr(RateExeption):

    def __str__(self):
        return f'Неверный тип для оценки!'
    

class RateValueErorr(RateExeption):
    
    def __init__(self, min_value: int, max_value: int, value):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
      
    def __str__(self):
        return f"{self.value} вне диапазона [{self.min_value}, {self.max_value}]"


class TestRate:
    """Класс-дескриптор для проверки выставленных оценок."""

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        """Сохранить имя параметра."""
        self.param_name = name

    def __set__(self, instance, value):
        """Установка значения атрибута."""
        self._validate(value)
        instance.__dict__[self.param_name] = value
        # setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        """Получить значение атрибута"""
        return instance.__dict__[self.param_name]
        # getattr(instance, self.param_name)

    def _validate(self, value):
        """Валидация полученного значения."""
        if not isinstance(value, int):
            raise RateTypeErorr
        if not self.min_value <= value <= self.max_value:
            raise RateValueErorr(self.min_value, self.max_value, value)