# ЗАДАНИЕ 1: Работа с типами данных

text = "Привет"
number = 42
float_num = 3.14
my_list = [1, 2, 3]

print(type(text))
print(type(number))
print(type(float_num))
print(type(my_list))

# ЗАДАНИЕ 2: Преобразование регистра

line = "python PROGRAMMING"

print(line.lower())
print(line.upper())
print(line.capitalize())
print(line.title())

# ЗАДАНИЕ 3: Удаление пробелов

line = "  Hello World  "

print(line.strip())
print(line.lstrip())
print(line.rstrip())

# ЗАДАНИЕ 4: Разделение и объединение строк

fruits = "яблоко,банан,апельсин,груша"
fruits_list = fruits.split(",")
print(fruits_list)

joined = " | ".join(fruits_list)
print(joined)

# ЗАДАНИЕ 5: Замена подстрок

text = "Я изучаю Python. Python - это круто!"
print(text.replace("Python", "Java"))

# ЗАДАНИЕ 6: Поиск и подсчет

line = "Python программирование на Python"

print(line.find("Python"))
print(line.count("Python"))
print(line.find("Java"))

# ЗАДАНИЕ 7: Проверка типа символов

print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

# ЗАДАНИЕ 8: Срезы строк

line = "Python very good"

print(line[:3])
print(line[-3:])
print(line[::2])
print(line[::-1])

# ЗАДАНИЕ 9: Экранирование символов

print('Он сказал: "Привет"')
print("Первая строка\nВторая строка")

# ЗАДАНИЕ 10: Добавление элементов в список

fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")
print(fruits)

# ЗАДАНИЕ 11: Удаление элементов из списка

fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
last = fruits.pop()
print(fruits, last)

# ЗАДАНИЕ 12: Поиск в списке

fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index("банан"))
print(fruits.count("банан"))

# ЗАДАНИЕ 13: Сортировка и реверс

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print(numbers)

# БОНУСНОЕ 14

names = "Иван,Петр,Мария,Анна"
names_list = names.split(",")
names_list.append("Ольга")
names_list.sort()

result = ", ".join(names_list)
print(result)

# end
