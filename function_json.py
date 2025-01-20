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


new_note = create_user_data()
user_data.append(new_note)
save_data_to_file()