def search_notes(notes, keyword=None, status=None):
    if not notes:
        return []

    if keyword:
        notes = [
            note for note in notes
            if keyword.lower() in note.get('title', '').lower()
               or keyword.lower() in note.get('content', '').lower()
               or keyword.lower() in note.get('username', '').lower()
        ]

    if status:
        notes = [note for note in notes if note.get('status') == status]

    return notes

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

keyword_input = input("Введите ключевое слово для поиска: ").strip()
status_input = input("Введите статус для поиска (оставьте пустым, если не нужно): ").strip()

found_notes = search_notes(notes, keyword=keyword_input, status=status_input)

if found_notes:
    print("\nНайдены следующие заметки:\n")
    for note in found_notes:
        print(f"- {note['title']}")
else:
    print("\nПо вашему запросу заметки не найдены.")