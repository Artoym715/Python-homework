
import os

data_file = 'contacts.txt'
def print_commands():
    return print('Введите интересующую вас команду:'
                 '\n 1 - Показать все записи\n 2 - Поиск\n 3 - Добавить контакт\n 4 - Удалить контакт'
                 '\n 5 - Редактировать контакт\n 0 - Выход')

def read_data(file):
    with open(file, 'r', encoding="utf-8") as data:
        phone_book = []
        for line in data:
            phone_book.append(line.strip('\n').replace(',', ' '))
    return phone_book

def write_data(file, phone_book):
    with open(file, 'w', encoding="utf-8") as data:
        for line in phone_book:
            data.write(line.replace(' ', ',') + '\n')
        return print('Данные сохранены')


def show_all():
    phone_book = read_data(data_file)
    for line in phone_book:
        print(line)
    return


def search():
    find = input('Введите букву или строку для поиска: ')
    list1 = []
    phone_book = read_data(data_file)
    for line in phone_book:
        if find in line:
            list1.append(line)
    if list1 == []:
        return print("Ничего не найдено, попробуйте ешё раз")
    for line in list1:
        print(line)
    return


def add_record():
    phone_book = read_data(data_file)
    max_num = 0
    for i in phone_book:
        if max_num < int(i[0]):
            max_num = int(i[0])
    print('Добавьте данные')
    number = str(max_num + 1)
    surname = input('Введите фамилию: ').capitalize()
    name_first = input('Введите имя: ').capitalize()
    name_second = input('Введите отчество: ').capitalize()
    phonenumber = input('Введите номер телефона: ')
    n = '\n'
    phone_book.append(str(number) + ',' + str(surname) + ',' + str(name_first) + ',' + str(name_second) + ',' + str(phonenumber))
    write_data(data_file, phone_book)

def del_record():
    del_num = input('Введите идентефикатор удаляемой записи: ')
    phone_book = read_data(data_file)
    for line in phone_book:
        if line[0] == del_num:
            print(line)
            confirm = input('Введите "Y" для подтверждения или "N" для отмены: ')
            if confirm == 'Y':
                phone_book.pop(phone_book.index(line))
                write_data(data_file, phone_book)
                print('Контакт удалён')
                return
            return
    return print('Контакт не найден')

def edit_record():
    edit = input('Введите идентефикатор редактируемой записи: ')
    phone_book = read_data(data_file)
    for line in phone_book:
        if line[0] == edit:
            print(line)
            confirm = input('Введите "Y" для подтверждения или "N" для отмены: ')
            if confirm == 'Y':
                edit_num = int(input('Какую запись запись желаете отредактировать?\n'
                      '1 - Фамилию, 2 - Имя, 3 - Отчество, 4 - Номер телефона: '))
                if edit_num == 1:
                    new_surname = input('Введите фамилию: ').capitalize()
                    new_name_first = parse(2, line)
                    new_name_second = parse(3, line)
                    new_phonenumber = parse(4, line)
                elif edit_num == 2:
                    new_surname = parse(1, line)
                    new_name_first = input('Введите имя: ').capitalize()
                    new_name_second = parse(3, line)
                    new_phonenumber = parse(4, line)
                elif edit_num == 3:
                    new_surname = parse(1, line)
                    new_name_first = parse(2, line)
                    new_name_second = input('Введите отчество: ').capitalize()
                    new_phonenumber = parse(4, line)
                elif edit_num == 4:
                    new_surname = parse(1, line)
                    new_name_first = parse(2, line)
                    new_name_second = parse(3, line)
                    new_phonenumber = input('Введите номер телефона: ')
                else:
                    return print('Некоректный код команды')

                phone_book[phone_book.index(line)] = (str(edit) + ',' + str(new_surname)
                                                      + ',' + str(new_name_first) + ',' + str(new_name_second)
                                                      + ',' + str(new_phonenumber))
                write_data(data_file, phone_book)
                return
    return print('Контакт не найден')



def parse(number_name, line):
    count = 0
    result = ''
    for word in line:
        if word == ' ':
            count += 1
        if word != ' ':
            if count == number_name:
                result += word
    return result


clear = lambda: os.system('cls')
clear()
print('Добрый день!')

while True:
    print_commands()
    enter_num = int(input())
    if enter_num == 1:
        show_all()
    elif enter_num == 2:
        search()
    elif enter_num == 3:
        add_record()
    elif enter_num == 4:
        del_record()
    elif enter_num == 5:
        edit_record()
    elif enter_num == 0:
        exit()
    else:
        print('Неверный код команды')