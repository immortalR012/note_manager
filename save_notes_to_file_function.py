file = open(' filename.txt','w', encoding='utf-8')
from datetime import datetime

# Получение текущей даты
today = datetime.now().date()

# Получение данных от пользователя
name = input('Введите имя:')
title = input('Введите заголовок:')
content = input('Напишите заметку:')
issue_date = input('Введите дату истечения срока заметки (число месяц год): ')

try:
    issue_date_obj = datetime.strptime(issue_date, '%d %m %Y').date()
except ValueError as e:
    print(f'Ошибка при вводе даты: {e}')
    exit()  # Завершение программы при ошибке ввода даты

# Создание словаря с данными заметки
notes = {
    'name': name,
    'title': title,
    'content': content,
    'issue_date': issue_date_obj
}
while notes:
    file.write(f"{notes}\n")
    break
file.close()