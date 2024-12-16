
from datetime import datetime
created_date=input('ведите дату для создания заметки')
issue_date=input('ведите дату истечения срока заметки')
title=input('ведите заголовок вашей заметки')
created_date_obj = datetime.strptime(created_date, " %d %m %Y")
issue_date_obj = datetime.strptime(issue_date, " %d %m %Y")
print(created_date_obj.day,issue_date_obj.day)
print(created_date_obj.day,issue_date_obj.month)
print('ваша заметка'+ title)

