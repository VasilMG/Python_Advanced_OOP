class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


    def __str__(self): 
        return f'{self.name} is written by {self.author} and it is {self.pages}'

b = Book('Franklin', 'Nekoya kanadka', 200)

print(str(b))

