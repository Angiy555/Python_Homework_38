#Задание 38
"""
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
"""
import os

os.system('CLS')

def show_all(file_name:str):
    """
    Функция принимает имя файла  (file_name) в иде строки
    и выводит телефонную книгу на экран
    """
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = sorted(fd.readlines())
        print_data(data)
    input("\n--- нажмите enter для продолжения ---")

def add_new(file_name: str):
    """
    Функция принимает имя файла  (file_name) в виде строки
    запрашивает у пользователя данные в виде ФИО и номер телефона
    и сохраняет полученные данные в файл
    """
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    #Открытие файла и запись в него данных в конце файла
    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')
    

def find_by_atribute(file_name:str):
    """
    Функция принимает имя файла  (file_name) в виде строки
    запрашивает атрибут поиска и выводит результат поиска
    """    
    find_data = []
    atribute = input("Введите данные для поиска: ")
    print()
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = sorted(fd.readlines())
        for i in data:
            if atribute in i:
                find_data.append(i)
                
        if len(find_data) != 0:
            print_data(find_data)
        else:
            print('Такой записи нет в справочнике')
        
    input("\n--- нажмите enter для продолжения ---")

def modify_data(file_name):
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = sorted(fd.readlines())
        print_data(data)
        num_contact = int(input('Введите номер контакта для изменения или 0 для выхода: '))
        if num_contact != 0:
            last_name = input('Введите новую фамилию: ')
            first_name = input('Введите новое имя: ')
            patronymic = input('Введите новое отчество: ')
            phone_number = input('Введите новый номер: ')
            data[num_contact - 1] = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
            with open(file_name, "w", encoding="UTF-8") as fd:
                fd.write("".join(data))
                print("\nКонтакт изменен!")
                input("\n--- нажмите enter для продолжения ---")
        else:
            return

def remove_data(file_name):
    with open(file_name, 'r',encoding='utf-8') as fd:
        data = sorted(fd.readlines())
        print_data(data)
        num_contact = int(input('Введите номер контакта для удаления или 0 для выхода: '))
        if num_contact != 0:
            
            data.pop(num_contact - 1)
            with open(file_name, "w", encoding="UTF-8") as fd:
                fd.write("".join(data))
                print("\nКонтакт удален!")
                input("\n--- нажмите enter для продолжения ---")
        else:
            return

def print_data(data):
    phone_book = []
    person_ID = 1
    split_line = "=" * 70    
    print(split_line)
    print(" №  Фамилия        Имя          Отчество          Номер телефона")
    print(split_line)
    for contact in data:
        last_name, first_name, patronymic, phone_number = contact.split(", ")
        phone_book.append(
            {
                "ID": person_ID,
                "last_Name": last_name,
                "first_name": first_name,
                "patronymic": patronymic,
                "phone_number": phone_number,
            }
        )
        person_ID += 1

    for contact in phone_book:
        person_ID, last_name, first_name, patronymic, phone_number = contact.values()
        print(f"{person_ID:>1}. {last_name:<15} {first_name:<12} {patronymic:<15}  {phone_number:<10}")

    print(split_line)

def draw_interface ():
    """
    Функция рисования меню
    """
    split_line = "=" * 45
    print('#########     ТЕЛЕФОННАЯ КНИГА      #########')
    print(split_line)
    print('########            МЕНЮ            #########')
    print(split_line)
    print('1 - Показать все записи телефонной книги')
    print('2 - Добавить контакт в телефонную книгу')
    print('3 - Поиск контакта в телефонной книге')
    print('4 - Редактировать контакт в телефонной книге')
    print('5 - Удалить запись из телефонной книги')
    print('0 - Выход из программы')
    print(split_line)

def main():
    """
    Основная функция
    """
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        os.system('CLS')
        draw_interface()
        answer = input('Введите операцию от 1 до 5 или 0 для выхода: ')
        if answer == '1':
            os.system('CLS')
            show_all(file_name)
        elif answer == '2':
            os.system('CLS')
            add_new(file_name)
        elif answer == '3':
            os.system('CLS')
            find_by_atribute(file_name)
        elif answer == '4':
            modify_data(file_name)
        elif answer == '5':
            remove_data(file_name)
        elif answer == '0':
           flag_exit = True


if __name__ == '__main__':
    main()