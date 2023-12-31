# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# doctest,
# через assert ы
# unittest - по желанию
# pytest - по желанию

def check_number(num: int, min: int, max: int):
    """
    >>> check_number(5, 0, 100000)
    Число является простым
    >>> check_number(4, 0, 100000)
    Число является составным
    >>> check_number(-1, 0, 100000)
    Введённое число не входит в заданный диапазон
    """

    divider = 2
    count = 0

    if (num >= min and num <= max):
        for i in range(divider, num - 1):
            if (num% i == 0):
                count += 1
        if (count <= 0):
            print("Число является простым")
        else:
            print("Число является составным")
    else:
        print("Введённое число не входит в заданный диапазон")

def change_to_hex(number: int) -> str:
    """
    >>> change_to_hex(5)
    "result='5'"
    >>> change_to_hex(1204)
    "result='4B4'"
    """

    HEX = 16
    TEN16 = "A"
    ELEVEN16 = "B"
    TWELVE16 = "C"
    THIRTEEN16 = "D"
    FOURTEEN16 = "E"
    FIFTEEN16 = "F"

    result: str = ""
    while number > 0:
        temp_result: int = number % HEX
        match temp_result:
            case 10:
                result = TEN16 + result
            case 11:
                result = ELEVEN16 + result
            case 12:
                result = TWELVE16 + result
            case 13:
                result = THIRTEEN16 + result
            case 14:
                result = FOURTEEN16 + result
            case 15:
                result = FIFTEEN16 + result
            case _:
                result = str(temp_result) + result
        number //= HEX
    return f'{result=}'


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
