import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Neil Gaiman")
author_repository.save(author1)
author2 = Author("H.P. Lovecraft")
author_repository.save(author2)

author_repository.select_all()

book_1 = Book("American Gods", author1, "Fantasy")
book_repository.save(book_1)

book_2 = Book("Sandman", author1, "Fantasy")
book_repository.save(book_2)

book_3 = Book("The Dunwich Horror", author2, "Cosmic Horror")
book_repository.save(book_3)

book_4 = Book("The Shadow Over Innsmouth", author2, "Cosmic Horror")
book_repository.save(book_4)

pdb.set_trace()
