# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). Тут тоже добавить дескрипторы.
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

from Clases.education import Student
from Clases.disciplines import Discipline

if __name__ == '__main__':
    student_1 = Student('Иванов', 'Николай', 'Петрович')
    student_2 = Student('Петров', 'Сергей', 'Михайлович')
    student_3 = Student('Заляцкая', 'Татьяна', 'Михайловна')
    student_4 = Student('Гончарова', 'Мария', 'Петровна')

    # print(student_1)
    # print(student_2)
    # print(student_3)
    # print(student_4)

    # Добавить дисциплины
    student_1.append_to_progress(Discipline('Математика', 2, 10))
    student_1.append_to_progress(Discipline('Физика', 5, 50))
    student_1.append_to_progress(Discipline('Химия', 3, 30))

    print(student_1.short_name)
    print(student_1.show_progress())

    student_2.append_to_progress(Discipline('Химия', 4, 30))
    # student_2.append_to_progress(Discipline('Биология', 5, 50)) проверка на недопустимую дисциплину

    print(student_2.short_name)
    print(student_2.show_progress())

    student_3.append_to_progress(Discipline('Математика', 3, 20))
    student_3.append_to_progress(Discipline('Физика', 5, 50))
    student_3.append_to_progress(Discipline('Химия', 5, 50))

    print(student_3.short_name)
    print(student_3.show_progress())

    student_4.append_to_progress(Discipline('Математика', 4, 40))
    student_4.append_to_progress(Discipline('Физика', 4, 40))
    student_4.append_to_progress(Discipline('Химия', 3, 30))

    print(student_4.short_name)
    print(student_4.show_progress())

    student_1.save_progress()
    # Удалить Иванова
    del student_1

    # Создать Иванова заново - Дисциплины должны подгрузиться из файла
    student_1_1 = Student('Иванов', 'Николай', 'Петрович')
    print(student_1_1.short_name)
    print(student_1_1.show_progress())