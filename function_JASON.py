from datetime import datetime
import json

# Инициализация списка для хранения данных
user_data = []


# Функция для загрузки данных из файла
def load_data_from_file(file_path='data.json'):
    global user_data

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        pass  # Если файла нет, то просто продолжаем работу без данных
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON. Файл может быть поврежден.")


# Функция для сохранения данных в файл
def save_data_to_file(file_path='data.json'):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(user_data, file, ensure_ascii=False, indent=4)


# Загружаем данные из файла при старте программы
load_data_from_file()


def create_user_data():
    """Функция для создания новой заметки"""
    name = input('Введите имя: ')
    title = input('Введите заголовок: ')
    content = input('Введите заметку: ')

    # Ввод и проверка корректности даты
    while True:
        issue_date_str = input('Введите дату истечения срока заметки (ДД ММ ГГГГ): ')
        try:
            issue_date_obj = datetime.strptime(issue_date_str, '%d %m %Y')
            break
        except ValueError as e:
            print(f"Ошибка при преобразовании даты: {e}. Попробуйте снова.")

    # Создание словаря с данными
    note = {
        'имя': name,
        'заголовок': title,
        'заметка': content,
        'срок истечения заметки': issue_date_obj.strftime('%d %m %Y')  # Сохраняем дату в формате строки
    }
    return note


def update_user_data(index):
    if index >= len(user_data) or index < 0:
        print("Заметка с таким индексом не существует.")
        return

    note = user_data[index]
    print(f"Текущие данные заметки:\n{note}")

    name = input('Введите новое имя (оставьте пустым, чтобы не менять): ') or note['имя']
    title = input('Введите новый заголовок (оставьте пустым, чтобы не менять): ') or note['заголовок']
    content = input('Введите новую заметку (оставьте пустым, чтобы не менять): ') or note['заметка']

    # Обновление даты
    while True:
        issue_date_str = input(
            'Введите новую дату истечения срока заметки (ДД ММ ГГГГ), оставьте пустым, чтобы не менять: ')
        if not issue_date_str:
            issue_date_str = note['срок истечения заметки']  # Оставляем старую дату
            break
        try:
            issue_date_obj = datetime.strptime(issue_date_str, '%d %m %Y')
            issue_date_str = issue_date_obj.strftime('%d %m %Y')
            break
        except ValueError as e:
            print(f"Ошибка при преобразовании даты: {e}. Попробуйте снова.")

    updated_note = {
        'имя': name,
        'заголовок': title,
        'заметка': content,
        'срок истечения заметки': issue_date_str
    }
    user_data[index] = updated_note
    print("Заметка успешно обновлена!")
    save_data_to_file()  # Сохранение изменений в файл


def delete_user_data(index):
    """Функция для удаления заметки"""
    if index >= len(user_data) or index < 0:
        print("Заметка с таким индексом не существует.")
        return

    del user_data[index]
    print("Заметка успешно удалена!")
    save_data_to_file()  # Сохранение изменений в файл


def show_menu():
    """Функция для отображения меню"""
    print('\nВыберите действие:')
    print('"1" Создать новую заметку')
    print('"2" Изменить заметку')
    print('"3" Удалить заметку')
    print('"0" Выйти из программы')


def main():
    while True:
        show_menu()
        choice = input()

        if choice == '1':
            new_data = create_user_data()
            if new_data:
                user_data.append(new_data)
                print("Заметка успешно создана!")
                save_data_to_file()  # Сохранение новых данных в файл

        elif choice == '2':
            if not user_data:
                print("Нет заметок для изменения.")
                continue
            for i, note in enumerate(user_data):
                print(f"{i + 1}. {note['заголовок']} ({note['имя']})")
            index = int(input("Введите номер заметки для изменения: ")) - 1
            update_user_data(index)

        elif choice == '3':
            if not user_data:
                print("Нет заметок для удаления.")
                continue
            for i, note in enumerate(user_data):
                print(f"{i + 1}. {note['заголовок']} ({note['имя']})")
            index = int(input("Введите номер заметки для удаления: ")) - 1
            delete_user_data(index)

        elif choice == '0':
            print("До свидания!")
            break


if __name__ == "__main__":
    main()