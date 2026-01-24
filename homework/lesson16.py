class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return self.pages > 300


book1 = Book("Война и мир", "Толстой", 1225)
book2 = Book("1984", "Оруэлл", 328)
book3 = Book("Маленький принц", "Экзюпери", 96)

print(book1.get_info())
print(book1.is_long())
print(book2.get_info())
print(book2.is_long())
print(book3.get_info())
print(book3.is_long())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        print("Недостаточно средств")
        return False

    def get_balance(self):
        return self.balance


account = BankAccount(owner="Дмитрий", balance=1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
print("Баланс:", account.get_balance())
