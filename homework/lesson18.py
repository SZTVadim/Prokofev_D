from abc import ABC, abstractmethod


# ЧАСТЬ 1: Абстракция
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# ЧАСТЬ 2: Наследование
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


# ЧАСТЬ 3: Инкапсуляция
class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []  # приватный список животных

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        # геттер: даёт доступ к информации о приватном атрибуте
        return len(self.__animals)

    def get_animals(self):
        # удобно для перебора животных снаружи (не отдаём __animals напрямую)
        return self.__animals


# ЧАСТЬ 4: Полиморфизм
def animal_sound(animal):
    # Это полиморфизм: функция работает с любым объектом Animal,
    # и не важно, Dog это или Cat — у обоих есть make_sound(),
    # но реализация разная.
    animal.make_sound()


# 6) Создаём животных
dog1 = Dog("Тузик", 3)
dog2 = Dog("Стасик", 5)
cat1 = Cat("Евгений", 2)

# 7) Создаём зоопарк
zoo = Zoo("Зоопарк")

# 8) Добавляем животных
zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

# 9) Выводим количество животных
print("Количество животных в зоопарке:", zoo.get_animals_count())

# 10) Перебираем всех животных и вызываем звук (полиморфизм)
for animal in zoo.get_animals():
    animal_sound(animal)

# 11) Попытка создать Animal напрямую:
# animal = Animal()
# Произойдёт ошибка, потому что Animal — абстрактный класс.
# Пока make_sound() не реализован, Python не позволяет
# создавать объект такого класса.
