def update_note():
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
             'issue_date': issue_date, }
choice = input('хотите изменить заметку? нажмите "y/n"')

while choice == "y":
    print("Хотите изменить заметку? Нажмите \"y\"/\"n\": ")
    if choice == "y":
        print("\n1 Имя\n2 Заголовок\n3 Заметку\n4 Дату\n5 сохранить и выйти")
        parameter = int(input("Выберите параметр: "))

    if parameter == 1:
        new_name = input("Введите новое имя: ")
        user_data['name'] = new_name
    elif parameter == 2:
        new_title = input("Введите новый заголовок: ")
        user_data['title'] = new_title
    elif parameter == 3:
        new_content = input("Введите новую заметку: ")
        user_data['content'] = new_content
    elif parameter == 4:
        new_issue_date = input("Введите новую дату (число месяц год): ")
        user_data['issue_date'] = new_issue_date
        user_data['issue_date_obj'] = datetime.strptime(new_issue_date, "%d %m %Y")
    elif parameter == 5:
        print('изменения сохранить')
        break

print( user_data)
