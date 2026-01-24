# Тема: Функции и условные конструкции в Python

# ЗАДАНИЕ 1: Функции и условия


def calculate_total(price, tax_percent):
    if price < 0 or tax_percent > 20:
        return "Ошибка: некорректные данные"

    return price + price * tax_percent / 100


def get_level(points):
    if points >= 100:
        return "Эксперт"
    if points >= 50:
        return "Продвинутый"
    if points >= 20:
        return "Начинающий"
    return "Новичок"


# ЗАДАНИЕ 2: Функции с условиями и match/case


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"


# Проверки
print(calculate_total(100, 10))
print(calculate_total(-5, 10))
print(get_level(10))
print(get_level(60))
print(process_status("active"))
print(process_status("unknown"))
