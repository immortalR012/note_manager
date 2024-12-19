from datetime import datetime
username= input(' ведите имя')
second_mane=input(' ведите фамилию')
status=input('род дейтельности')
created_date=input('ведите дату для создания заметки')
issue_date=input('ведите дату истечения срока заметки')
title=input('ведите заголовок вашей заметки')
created_date_obj=datetime.strptime(created_date," %d %m %Y")
issue_date_obj=datetime.strptime(issue_date," %d %m %Y")
morning=input('ведите время затрака')
lunch=input('ведите время обеда')
dinner=input('ведите время ужина')
morning_obj=datetime.strptime(morning," %H %M %S")
lunch_obj=datetime.strptime(lunch," %H %M %S")
dinner_obj=datetime.strptime(dinner," %H %M %S")
print("дата создания",created_date_obj.day,issue_date_obj.day)
print("дата окончания",created_date_obj.day,issue_date_obj.month)
#print('ваша заметка '+ title)
#print(morning_obj.hour,lunch_obj.hour,dinner_obj.hour)
#print(morning_obj.minute,lunch_obj.minute,dinner_obj.minute)
#print(username)
#print(second_mane)
#print(status)
my_data=["имя",username,"фамилия",second_mane,"род занятий",status]
my_day=[title,'завтрак ',morning,'обед',lunch,'ужин',dinner]
my_mumber=[created_date,issue_date]
user_titles=[my_mumber,my_data,my_day]
#print(my_data)
#print(my_day)
heading_list={
    "mane":my_data,
    "time":my_mumber,
    "mode":my_day,
}
print(user_titles)
print(heading_list)
