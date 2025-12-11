# Задача 1 #

cubes = [x**3 for x in range(1, 9)]
print("Кубы:", cubes)
print("Минимум:", min(cubes))
print("Максимум:", max(cubes))

# Задача 2 #

numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
filtered = [n for n in numbers if n > 10]
print("Числа больше 10:", filtered)
print("Сумма:", sum(filtered))

# Задача 3 #

cities = ["москва", "санкт-петербург", "казань"]
capitalized = [city.title() for city in cities]
print("Города:", capitalized)
