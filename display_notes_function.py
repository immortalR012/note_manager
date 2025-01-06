def display_notes(notes):
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    for ind in range(len(notes)):
        note = notes[ind]
        print(f'\nЗаметка №{ind + 1}:')
        print(f'Имя пользователя: {note["username"]}')
        print(f'Заголовок: {note["title"]}')
        print(f'Описание: {note["description"]}')
        print(f'Статус: {note["status"]}')
        print(f'Дата создания: {note["creation_date"]}')
        print(f'Дедлайн: {note["deadline"]}')


# Определение списка заметок вне функции
notes = [
    {
        'username': 'Алексей',
        'title': 'Список покупок',
        'description': 'Купить продукты на неделю',
        'status': 'новая',
        'creation_date': '27-11-2024',
        'deadline': '30-11-2024'
    },
    {
        'username': 'Анна',
        'title': 'Подготовить отчет',
        'description': 'Отчет по проекту за квартал',
        'status': 'в процессе',
        'creation_date': '01-12-2024',
        'deadline': '05-12-2024'
    }
]
display_notes(notes)