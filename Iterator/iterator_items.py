from collections.abc import Iterable, Iterator

# Aggregate: 集約オブジェクト
class Menu(Iterable):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        return MenuIterator(self)

# Concrete Aggregate: 具体的な集約オブジェクト
class MenuItem:
    def __init__(self, name):
        self.name = name

# Iterator: イテレータ
class MenuIterator(Iterator):
    def __init__(self, menu):
        self.menu = menu
        self.index = 0

    def __next__(self):
        if self.index < len(self.menu.items):
            item = self.menu.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Client コード
def main():
    menu = Menu()
    menu.add_item(MenuItem("Item 1"))
    menu.add_item(MenuItem("Item 2"))
    menu.add_item(MenuItem("Item 3"))

    iterator = iter(menu)
    while True:
        try:
            item = next(iterator)
            print(item.name)
        except StopIteration:
            break

if __name__ == "__main__":
    main()
