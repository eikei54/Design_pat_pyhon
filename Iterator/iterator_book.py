from abc import ABC, abstractmethod

# Aggregate インタフェースの定義
class Aggregate(ABC):
    @abstractmethod
    def iterator(self):
        pass

# Book クラスの定義
class Book:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

# BookShelf クラスの定義
class BookShelf(Aggregate):
    def __init__(self, initialize):
        self.books = []

    def get_book_at(self, index):
        return self.books[index]

    def append_book(self, book):
        self.books.append(book)

    def get_length(self):
        return len(self.books)

    def iterator(self):
        return BookShelfIterator(self)

# BookShelfIterator クラスの定義
class BookShelfIterator:
    def __init__(self, book_shelf):
        self.book_shelf = book_shelf
        self.index = 0

    def has_next(self):
        return self.index < self.book_shelf.get_length()

    def next(self):
        book = self.book_shelf.get_book_at(self.index)
        self.index += 1
        return book

def main():
    # テスト用のコードをここに記述
    book_shelf = BookShelf(10)
    book_shelf.append_book(Book("Book 1"))
    book_shelf.append_book(Book("Book 2"))
    book_shelf.append_book(Book("Book 3"))

    iterator = book_shelf.iterator()
    while iterator.has_next():
        book = iterator.next()
        print("Book Name:", book.get_name())

if __name__ == "__main__":
    main()
