def create_note():
    name = input("Введите имя заметки: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (например, 'Новая', 'В процессе', 'Завершенная'): ")
    creation_date = input("Введите дату создания заметки (в формате ДД.ММ.ГГГГ): ")
    deadline = input("Введите дедлайн заметки (в формате ДД.ММ.ГГГГ): ")

    note = {
        "name": name,
        "title": title,
        "description": description,
        "status": status,
        "creation_date": creation_date,
        "deadline": deadline
    }

    return note


def display_notes(notes):
    """Функция для вывода всех заметок"""

    if not notes:
        print("\nСписок заметок пуст.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"\nЗаметка {i}:")
        for key, value in note.items():
            print(f"{key.capitalize()}: {value}")


def main():
    notes = []

    while True:
        user_input = input("\nХотите создать новую заметку? (да/нет): ").lower()

        if user_input == "да":
            new_note = create_note()
            notes.append(new_note)

            print("\nЗаметка успешно создана!")
        elif user_input == "нет":
            break
        else:
            print("Неизвестный ответ. Пожалуйста, введите 'да' или 'нет'.")

    display_notes(notes)


if __name__ == "__main__":
    main()
