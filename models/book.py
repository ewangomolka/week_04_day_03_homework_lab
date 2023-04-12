class Book:

    def __init__(self, title, author, genre, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.id = id

    def mark_complete(self):
        self.completed = True
