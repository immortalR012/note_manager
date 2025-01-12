import datetime

def get_user_input():
    today = datetime.datetime.now().date()
    name = input('Введите имя: ')
    title = input('Введите заголовок: ')
    content = input('Напишите заметку: ')
    issue_date_str = input('Введите дату истечения срока заметки (число месяц год): ')

    try:
        issue_date_obj = datetime.datetime.strptime(issue_date_str, '%d %m %Y').date()
    except ValueError as e:
        print(f'Ошибка при вводе даты: {e}')
        return None

    note = {
        'name': name,
        'title': title,
        'content': content,
        'issue_date': issue_date_obj
    }
    return note


def save_note(note):
    try:
        with open('filename.txt', 'a', encoding='utf-8') as file:
            file.write(f"{note}\n")
    except FileNotFoundError:
        print('Файл не найден.')
    except PermissionError:
        print('Нет доступа к файлу.')


def load_notes_from_file():
    try:
        with open('filename.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line())
    except FileNotFoundError:
        print('Файл не найден.')


if __name__ == "__main__":
    note = get_user_input()
    if note:
        save_note(note)
    load_notes_from_file()