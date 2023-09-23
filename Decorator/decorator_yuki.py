# The equivalent of the abstract class in Java is achieved in Python using the ABC module
from abc import ABC, abstractmethod

# This is equivalent to the Display abstract class in Java
class Display(ABC):
    @abstractmethod
    def get_columns(self):
        pass

    @abstractmethod
    def get_rows(self):
        pass

    @abstractmethod
    def get_row_text(self, row):
        pass

    # This is equivalent to the show method in the Display abstract class in Java
    def show(self):
        for i in range(self.get_rows()):
            print(self.get_row_text(i))

# This is equivalent to the Border abstract class in Java
class Border(Display, ABC):
    def __init__(self, display):
        self.display = display

# This is equivalent to the FullBorder class in Java
class FullBorder(Border):
    def __init__(self, display):
        super().__init__(display)

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0:
            return "+" + self.make_line('-', self.display.get_columns()) + "+"
        elif row == self.display.get_rows() + 1:
            return "+" + self.make_line('-', self.display.get_columns()) + "+"
        else:
            return "|" + self.display.get_row_text(row - 1) + "|"

    @staticmethod
    def make_line(ch, count):
        return ch * count

# This is equivalent to the SideBorder class in Java
class SideBorder(Border):
    def __init__(self, display, ch):
        super().__init__(display)
        self.border_char = ch

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return self.display.get_rows()

    def get_row_text(self, row):
        return self.border_char + self.display.get_row_text(row) + self.border_char

# This is equivalent to the StringDisplay class in Java
class StringDisplay(Display):
    def __init__(self, string):
        self.string = string

    def get_columns(self):
        return len(self.string)

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        if row != 0:
            raise IndexError()
        return self.string

# This is equivalent to the Main class in Java
def main():
    b1 = StringDisplay("Hello, world.")
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b1.show()
    b2.show()
    b3.show()

    b4 = SideBorder(FullBorder(FullBorder(SideBorder(FullBorder(StringDisplay("Hello, world.")), '*'))), '/')

    b4.show()

if __name__ == "__main__":
    main()
