# The equivalent of the abstract class in Java is achieved in Python using the ABC module
from abc import ABC, abstractmethod

# This is equivalent to the AbstractDisplay abstract class in Java
class AbstractDisplay(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    # This is equivalent to the display method in the AbstractDisplay abstract class in Java
    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()

# This is equivalent to the CharDisplay class in Java
class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print("<<", end="")

    def print(self):
        print(self.ch, end="")

    def close(self):
        print(">>")

# This is equivalent to the StringDisplay class in Java
class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def open(self):
        self.print_line()

    def print(self):
        print("|" + self.string + "|")

    def close(self):
        self.print_line()

    def print_line(self):
        print("+" + "-" * self.width + "+")

# This is equivalent to the Main class in Java
def main():
    d1 = CharDisplay('H')
    d2 = StringDisplay("Hello, world.")

    d1.display()
    d2.display()

if __name__ == "__main__":
    main()
