from date_create import *
import datetime
import json
import os.path
import re

def create_note():
    id = "1"
    title = input_title()
    note = input_note()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {id: {"Заголовок": title, "Заметка": note, "Дата": date}}

def add_note(note):
    if os.path.getsize('notes.json') == 0:
        with open('notes.json', 'a', encoding='UTF-8') as file:
            data = {}
            data['Ваши заметки'] = []
            data['Ваши заметки'].append(note)
            json.dump(data, file, ensure_ascii = False, sort_keys=True, indent=2)
    else:
        with open('notes.json', 'r', encoding='UTF-8') as file:
            data = json.load(file)
            new_id = str(len(data['Ваши заметки']) + 1)
            note[new_id] = note.pop("1")
            data['Ваши заметки'].append(note)
        with open('notes.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii = False, sort_keys=True, indent=2)

def show_info():
    with open('notes.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        notes = data['Ваши заметки']
        if len(notes) == 0:
            print('У вас нет заметок')
            print()
        else:
            print('Ваши заметки: ')
            print()
            for note in notes:
                note_id = list(note.keys())
                print('Заметка ' + note_id[0])
                note_body = note[note_id[0]]
                for key in note_body:
                    print(key + ': ' + note_body[key])
                print()
            print()

def search_note():
    with open('notes.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        notes = data['Ваши заметки']
        if len(notes) == 0:
                print('У вас нет заметок')
                print()
        else:
            search = input('Введите дату для поиска в формате гггг-мм-дд: ')
            print()
            
            if not re.match('((19|20)\\d\\d)[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])', search):
                print('Неверный формат даты. Убедитесь что вводите дату в формате гггг-мм-дд')
                print()
            else:
                search_result = False

                for note in notes:
                    note_id = list(note.keys())
                    note_body = note[note_id[0]]
                    check_date = note_body['Дата'][:10]
                    
                    if search == check_date:
                        print("Заметка " + note_id[0])
                        search_result = True
                        for key in note_body:
                            print(key + ': ' + note_body[key])
                    print()

                if search_result != True:
                    print('По вашему запросу ничего не найдено')
                    print()

def edit_note():
    with open('notes.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        notes = data['Ваши заметки']
        if len(notes) == 0:
            print('У вас нет заметок')
            print()
        else:
            note_for_edit = int(input('Укажите номер заметки для редактирования: '))
            print()
            if note_for_edit > len(notes):
                print('Заметки с таким номером не существует')
                print()
            else:
                edited_note = create_note()
                index = int(note_for_edit) - 1
                edited_note[note_for_edit] = edited_note.pop("1")
                notes[index] = edited_note

                with open('notes.json', 'w', encoding='UTF-8') as file:
                    json.dump(data, file, ensure_ascii = False, sort_keys=True, indent=2)

                    print('Заметка изменена!')
                    print()            

def delete_note():
    with open('notes.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        notes = data['Ваши заметки']
        if len(notes) == 0:
            print('У вас нет заметок')
            print()
        else:
            note_for_delete = int(input('Укажите номер заметки для удаления: '))
            print()

            if note_for_delete > len(notes):
                print('Заметки с таким номером не существует')
                print()
            else:
                index = int(note_for_delete) - 1
                del notes[index]

                new_ID = "1"

                for note in notes:
                    note_id = list(note.keys())
                    note[new_ID] = note.pop(note_id[0])
                    new_ID = str(int(new_ID) + 1)

                with open('notes.json', 'w', encoding='UTF-8') as file:
                    json.dump(data, file, ensure_ascii = False, sort_keys=True, indent=2)

                    print('Заметка удалена!')
                    print()

        