# ЗАДАНИЕ 1: Работа с кортежами

coordinates = (10, 20, 30, 20, 10, 20, 40)

# 1. Выведите первый элемент кортежа
print(coordinates[0])

# 2. Выведите последний элемент кортежа
print(coordinates[-1])

# 3. Выведите срез со 2-го по 4-й элемент (включительно)
print(coordinates[1:4])

# 4. Проверьте, есть ли число 30 в кортеже
print(30 in coordinates)

# 5. Найдите индекс первого вхождения числа 20
print(coordinates.index(20))

# 6. Подсчитайте, сколько раз встречается число 20
print(coordinates.count(20))

# 7. Подсчитайте, сколько раз встречается число 50
print(coordinates.count(50))

# 8. Выведите длину кортежа
print(len(coordinates))


# ЗАДАНИЕ 2: Операции с кортежами

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]

# 1. Объедините tuple1 и tuple2
print(tuple1 + tuple2)

# 2. Повторите элементы tuple1 три раза
print(tuple1 * 3)

# 3. Распакуйте tuple1 в переменные a, b, c
a, b, c = tuple1
print(a, b, c)

# 4. Распакуйте numbers в first, middle, last
numbers_tuple = tuple(numbers)
first, *middle, last = numbers_tuple
print(first, middle, last)

# 5. Преобразуйте список numbers в кортеж
print(tuple(numbers))

# 6. Кортеж из четных чисел от 0 до 10
even_tuple = tuple(x for x in range(0, 11) if x % 2 == 0)
print(even_tuple)

# 7. Кортеж квадратов чисел от 1 до 5
squares_tuple = tuple(x**2 for x in range(1, 6))
print(squares_tuple)

# 8. Кортеж из одного элемента со значением 42
single_tuple = (42,)
print(single_tuple)
