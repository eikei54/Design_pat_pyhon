from abc import ABC, abstractmethod

class Banner:
    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        print("({})".format(self.string))

    def show_with_aster(self):
        print("*{}*".format(self.string))


class Print(ABC):
    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass


class PrintBanner(Banner, Print):
    def __init__(self, string):
        super().__init__(string)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


def main():
    p = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == "__main__":
    main()
