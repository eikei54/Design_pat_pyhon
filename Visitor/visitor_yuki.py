# Javaの抽象クラスはPythonではABCモジュールを使用して実現します
from abc import ABC, abstractmethod

# これはJavaのEntry抽象クラスに相当します
class Entry(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def __str__(self):
        return f"{self.get_name()} ({self.get_size()})"

# これはJavaのDirectoryクラスに相当します
class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []

    def get_name(self):
        return self.name

    def get_size(self):
        return sum(entry.get_size() for entry in self.directory)

    def add(self, entry):
        self.directory.append(entry)
        return self

    def __iter__(self):
        return iter(self.directory)

# これはJavaのFileクラスに相当します
class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

# これはJavaのListVisitorクラスに相当します
class ListVisitor:
    def __init__(self):
        self.currentdir = ""

    def visit(self, entry):
        if isinstance(entry, File):
            print(f"{self.currentdir}/{entry}")
        elif isinstance(entry, Directory):
            print(f"{self.currentdir}/{entry}")
            savedir = self.currentdir
            self.currentdir = f"{self.currentdir}/{entry.get_name()}"
            for ent in entry:
                self.visit(ent)
            self.currentdir = savedir

# これはJavaのMainクラスに相当します
def main():
    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")
    rootdir.add(bindir).add(tmpdir).add(usrdir)
    bindir.add(File("vi", 10000)).add(File("latex", 20000))

    yuki = Directory("yuki")
    hanako = Directory("hanako")
    tomura = Directory("tomura")
    usrdir.add(yuki).add(hanako).add(tomura)

    yuki.add(File("diary.html", 100)).add(File("Composite.java", 200))

    hanako.add(File("memo.tex", 300)).add(File("index.html", 350))

    tomura.add(File("game.doc", 400)).add(File("junk.mail", 500))

    list_visitor = ListVisitor()

    for entry in rootdir:
        list_visitor.visit(entry)

if __name__ == "__main__":
    main()
