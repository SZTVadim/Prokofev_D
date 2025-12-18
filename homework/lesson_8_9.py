# ЗАДАНИЕ 1

student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2,
    "город": "Москва"
}

print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, value)

for value in student.values():
    print(value)


# ЗАДАНИЕ 2

prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 40,
    "груша": 35,
    "виноград": 60
}

del prices["груша"]

grape_price = prices.pop("виноград")
print(grape_price)

discount_prices = {fruit: price * 0.9 for fruit, price in prices.items()}
print(discount_prices)


# ЗАДАНИЕ 3

student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

student1.update(student2)
print(student1)

student3 = student1.copy()
student3.update(student2)

print(student1)
print(student2)
print(student3)
