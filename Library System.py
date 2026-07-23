class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
        print(self.title,"Borrowed")
    def return_Book(self):
        self.is_borrowed = False
        print(self.title, "Returned")
obj_Book1 = Book("1984", "George Orwell")
obj_Book2 = Book("Art Of War", "Sun Tzu")

obj_Book1.borrow()
obj_Book1.return_Book()
obj_Book2.borrow()
obj_Book2.return_Book()