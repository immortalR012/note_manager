
def create_note():
    pass

from datetime import datetime


today = datetime.now()
name = input('ведите имя')
title = input('ведите заголовок')
content = input('напишите заметку')
issue_date = (input('ведите дату число месяц истечение срока заметки'))
issue_date_obj = datetime.strptime(issue_date, "%d %m %Y")
user_data = {'name': name,
             'title': title,
             'content': content,
             'issue_date': issue_date,
             }
try:
    issue_date_obj = datetime.strptime(issue_date, '%d %m %Y').date()
except ValueError as e:
    print('Ошибка при вводе даты: {e}')
else:
    user_data = {
        'name': name,
        'title': title,
        'content': content,
        'issue_date': issue_date_obj
    }
print(today.date())
print(user_data)

