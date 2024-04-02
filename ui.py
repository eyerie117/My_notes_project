from logger import *

def interface():    

    command = '-1'
    while command != '6':
        print('Выберете необходимое действие:\n'
            '1. Добавить заметку\n'
            '2. Вывести на экран список заметок\n'
            '3. Поиск заметки по дате\n'
            '4. Редактирование заметки\n'
            '5. Удаление заметок\n'
            '6. Выход из программы')        
        print()

        command = input('Выберете пункт меню: ')
        print()

        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод данных, выберете существующий пункт меню')
            command = input('Выберете пункт меню: ')

        match command: 
            case '1':
                add_note(create_note())
            case '2':
                show_info()
            case '3':
                search_note()
            case '4':
                edit_note()
            case '5':
                delete_note()
            case '6':
                print('Программа завершила свою работу')