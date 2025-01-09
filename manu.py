from create_note_function import create_note
from display_notes_function import display_notes
from update_note_function import update_note
from delete_note import delete_notes
from update_status import update_status


def main_menu():
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы\n")

        try:
            choice = int(input("Ваш выбор: "))

            if choice == 1:
                result = create_note()
                print(result)
            elif choice == 2:
                result = display_notes()
                print(result)
            elif choice == 3:
                result = update_note()
                print(result)
            elif choice == 4:
                result = delete_notes()
                print(result)
            elif choice == 5:
                result = update_status()
                print(result)
            elif choice == 6:
                print("Программа завершена. Спасибо за использование!")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите действие из списка.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите число от 1 до 6.")
