notes = [
    {
        'title': 'Задача 1',
        'author': 'Иван Иванов'
    },
    {
        'title': 'Задача 2',
        'author': 'Петр Петров'
    },
    {
        'title': 'Задача 3',
        'author': 'Иван Иванов'
    }
]


def delete_notes(criterion, value):
    deleted_count = 0
    for note in notes[:]:
        if note[criterion] == value:
            notes.remove(note)
            deleted_count += 1

    if deleted_count > 0:
        print(f"Удалено {deleted_count} заметок.")
    else:
        print("Ничего не было удалено. Записи с таким критерием отсутствуют.")


def main():
    while True:
        print("\nМеню:")
        print("1. Удалить заметку по имени пользователя")
        print("2. Удалить заметку по заголовку")
        print("3. Показать текущие заметки")
        print("4. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            author = input("Введите имя пользователя: ")
            delete_notes('author', author)
        elif choice == '2':
            title = input("Введите заголовок заметки: ")
            delete_notes('title', title)
        elif choice == '3':
            print("\nТекущие заметки:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note['title']} ({note['author']})")
        elif choice == '4':
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
