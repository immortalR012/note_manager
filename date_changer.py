from datetime import datetime
created_date=(input('ведите дату"число месяц"для создания заметки'))
issue_date=(input('ведите дату"число месяц" истечение срока заметки'))
created_date_obj = datetime.strptime(created_date, "%d %m %Y")
issue_date_obj = datetime.strptime(issue_date, "%d %m %Y")
print(created_date_obj.day,issue_date_obj.day)
print(created_date_obj.day,issue_date_obj.month)

