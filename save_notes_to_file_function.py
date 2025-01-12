file = open(' filename.txt','w', encoding='utf-8')
from datetime import datetime

today = datetime.now().date()

name = input('Введите имя:')
title = input('Введите заголовок:')
content = input('Напишите заметку:')
issue_date = input('Введите дату истечения срока заметки (число месяц год): ')

try:
    issue_date_obj = datetime.strptime(issue_date, '%d %m %Y').date()
except ValueError as e:
    print(f'Ошибка при вводе даты: {e}')
    exit()
notes = {
    'name': name,
    'title': title,
    'content': content,
    'issue_date': issue_date_obj
}

with open('filename.txt','w',encoding='utf-8') as file:
        file.write(f"{notes}\n")
def load_notes_from_file():
    with open('filename.txt', 'r', encoding='utf-8'):
        for f in file:
            print(f,end='')
file.close()
