from datetime import datetime


def validate_date(date_str):

    try:
        return datetime.strptime(date_str, '%d %m %Y')
    except ValueError:
        raise ValueError("Неверный формат даты! Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")


def main():
    current_date = datetime.now()

    while True:
        try:
            issue_date_str = input("Введите дату дедлайна в формате ДД-ММ-ГГГГ: ")
            issue_date = validate_date(issue_date_str)

            if issue_date.date() < current_date.date():
                print(f"Дедлайн истек {current_date.date() - issue_date.date()} дня назад!")
            elif issue_date.date() == current_date.date():
                print("Сегодня последний день для завершения работы!")
            else:
                days_left = issue_date.date() - current_date.date()
                print(f"До дедлайна осталось {days_left.days} дней.")

            break

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
