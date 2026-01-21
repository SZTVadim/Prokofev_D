# 1. Создайте список только положительных чисел

# 2. Создайте список, где отрицательные числа заменены на их модуль

# 3. Создайте кортеж из квадратов всех чисел

# 4. Найдите минимальное и максимальное значение

# 5. Создайте словарь, где ключ - число, а значение - "положительное" или "отрицательное"

# 6. Преобразуйте список в множество, чтобы убрать возможные дубликаты

numbers = [15, -8, 23, -5, 0, 42, -12, 7]
positive_number = [x for x in numbers if x > 0]
print(positive_number)

abs_numbers = [abs(x) for x in numbers if x < 0 ]
print(abs_numbers)

tuple_new = tuple(x ** 2 for x in numbers)
print(tuple_new)

print(min(numbers), max(numbers))

new_dict = {x: "положительное" if x > 0 else "отрицательное" if x < 0 else "ноль" for x in numbers}
print(new_dict)

number_set = set(numbers)
print(number_set)