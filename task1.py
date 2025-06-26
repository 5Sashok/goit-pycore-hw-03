from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворення вхідного рядка у дату
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Отримання поточної дати
        today_date = datetime.today().date()
        # Розрахунок різниці в днях
        delta = today_date - input_date
        return delta.days
    except ValueError:
        # Якщо дата у неправильному форматі — повідомлення про помилку
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")

# Приклад використання:
print(get_days_from_today("2025-06-06"))
