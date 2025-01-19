title=[]
while True:
    user= input("Введите заголовок заметки (или 'стоп' для завершения): ")
    title.append(user)
    if user== "стоп":
        break

    for new_title in title:
        print(new_title)