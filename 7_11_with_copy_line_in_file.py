

import csv
from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            # проверка на количество знаков в номере
            if len(str(phone_number)) != 11:
                print('Количество цифр в номере телефона неверное')
            else:
                flag = True
        except ValueError:
            print('Не валидный номер')

    return [first_name, last_name, phone_number]


# создание основного файла телефонной книги
def create_file(phonebook_file_name):
    with open(phonebook_file_name, "w", encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


# создание копии файла телефонной книги командой n
def create_new_file(second_file_to_copy):
    with open(phonebook_file_name, "w", encoding='utf-8', newline='') as data:
        file_write = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        file_write.writeheader()


# чтение основного файла телефонной книги командой r
def read_file(phonebook_file_name):
    with open(phonebook_file_name, "r", encoding='utf-8', newline='') as data:
        f_r = DictReader(data)
        return list(f_r)


# чтение копии файла командой rn
def read_new_file(second_file_to_copy):
    with open(second_file_to_copy, "r", encoding='utf-8', newline='') as file:
        file_read = csv.reader(file)
        for row in file_read:
            print(row)


def write_file(phonebook_file_name, lst):
    res = read_file(phonebook_file_name)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(phonebook_file_name, "w", newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def write_new_file(second_file_to_copy, lst_1):
    res1 = read_new_file(second_file_to_copy)
    obj1 = {'Имя': lst_1[0], 'Фамилия': lst_1[1], 'Телефон': lst_1[2]}
    res1.append(obj1)
    with open(second_file_to_copy, "w", newline='') as data:
        file_write = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        file_write.writeheader()
        file_write.writerows(res1)


phonebook_file_name = 'phone.csv'
second_file_to_copy = 'phonebook.csv'


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        # команда для создания нового файла-копии
        elif command == 'n':
            create_file(second_file_to_copy)

        # команда для чтения нового файла-копии
        elif command == 'rn':
            print(read_new_file(second_file_to_copy))

        # копирование выбранной пользователем строки в новый файл
        elif command == 'copy':

            file_line = int(input('Введите номер строки, которую нужно скопировать: '))
            with open(phonebook_file_name, mode='r', encoding='utf_8') as fr:

                line_1 = fr.readlines()[file_line]  # находим содержимое нужной строки
                result = {'Имя': line_1[0], 'Фамилия': line_1[1], 'Телефон': line_1[2]}  # записываем содержимое во временный список
            if len(line_1) > file_line:
                print(f'Cтрока {line_1} скопирована')

                with open(second_file_to_copy, 'w') as f:   # записываем содержиоме списка reault в новый файл
                    f.writelines(line_1)
            else:
                print('Строки с таким номером не существует')



        elif command == 'w':
            if not exists(phonebook_file_name):
                create_file(phonebook_file_name)
            write_file(phonebook_file_name, get_info())

        elif command == 'r':
            if not exists(phonebook_file_name):
                print('ФАЙЛ ОТСУТСТВУЕТ. СОЗДАЙТЕ ЕГО')
                continue
            print(*read_file(phonebook_file_name), sep=",\n", end="]\n")


main()

# def file_to_file_create(second_file_name):
#     with open('phone.csv') as source, open('phonebook.csv', 'w') as destination:
#         for line in source:
#             file_line = input('Введите номер строки, которую нужно скопировать: ')
#             line = file_line
#             destination.write(line)
