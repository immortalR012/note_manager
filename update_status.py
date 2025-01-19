from datetime import datetime

# Словарь для хранения статуса заметки
note_statuses = {
    1: "выполнено",
    2: "в процессе",
    3: "отложено"
}


# Функция для отображения текущего статуса заметки
def display_current_status(current_status):
    print(f"Текущий статус заметки: \"{current_status}\"")


# Функция для изменения статуса заметки
def change_status(current_status):
    print("\nВыберите новый статус заметки:")
    for key, value in note_statuses.items():
        print(f"{key}. {value}")

    while True:
        try:
            user_choice = int(input("Ваш выбор: "))
            if user_choice in note_statuses:
                break
            else:
                print("Пожалуйста, выберите правильный номер статуса.")
        except ValueError:
            print("Пожалуйста, введите число.")

    updated_status = note_statuses[user_choice]
    print(f"\nСтатус заметки успешно обновлен на: \"{updated_status}\"")
    return updated_status


# Функция для обработки дедлайнов
def check_deadline(issue_date):
    current_date = datetime.now().date()
    deadline_passed = issue_date < current_date
    if deadline_passed:
        print("Внимание! Срок выполнения заметки истек!")


# Основная функция программы
def main():
    # Предположим, что текущие данные уже существуют
    current_status = "в процессе"
    issue_date = datetime(2023, 10, 15).date()  # Дедлайн заметки

    display_current_status(current_status)
    check_deadline(issue_date)

    if input("Хотите изменить статус заметки? (да/нет): ").lower() == "да":
        current_status = change_status(current_status)

    print(f"\nОкончательный статус заметки: \"{current_status}\"")


