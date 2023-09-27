class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year
book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
book3 = Book("Евгений Онегин", "Александр Пушкин", 1833)

print("Название:", book1.get_title())
print("Автор:", book1.get_author())
print("Год издания:", book1.get_year())

print("Название:", book2.get_title())
print("Автор:", book2.get_author())
print("Год издания:", book2.get_year())

print("Название:", book3.get_title())
print("Автор:", book3.get_author())
print("Год издания:", book3.get_year())
