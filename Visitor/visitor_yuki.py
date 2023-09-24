#このPythonコードは、ファイルとディレクトリを表現するためのクラスを定義し、
# それらを使ってファイルシステムの階層構造を作成し、その構造を表示するものです。
# 以下に各部分の詳細な説明を追加します
# Javaの抽象クラスはPythonではABCモジュールを使用して実現します
from abc import ABC, abstractmethod

# これはJavaのEntry抽象クラスに相当します
class Entry(ABC):
    # get_nameとget_sizeは抽象メソッドで、具体的な実装はサブクラスで行います
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    # __str__メソッドはエントリの名前とサイズを文字列として返します
    def __str__(self):
        return f"{self.get_name()} ({self.get_size()})"

# これはJavaのDirectoryクラスに相当します
class Directory(Entry):
    def __init__(self, name):
        # ディレクトリ名とディレクトリ内のエントリリストを初期化します
        self.name = name
        self.directory = []

    # ディレクトリ名を返すメソッドです
    def get_name(self):
        return self.name

    # ディレクトリ内の全エントリのサイズの合計を返すメソッドです
    def get_size(self):
        return sum(entry.get_size() for entry in self.directory)

    # エントリをディレクトリに追加するメソッドです
    def add(self, entry):
        self.directory.append(entry)
        return self

    # ディレクトリ内のエントリをイテレートするためのメソッドです
    def __iter__(self):
        return iter(self.directory)

# これはJavaのFileクラスに相当します
class File(Entry):
    def __init__(self, name, size):
        # ファイル名とファイルサイズを初期化します
        self.name = name
        self.size = size

    # ファイル名を返すメソッドです
    def get_name(self):
        return self.name

    # ファイルサイズを返すメソッドです
    def get_size(self):
        return self.size

# これはJavaのListVisitorクラスに相当します
class ListVisitor:
    def __init__(self):
        # 現在訪れているディレクトリパスを保持する変数です
        self.currentdir = ""

    # エントリ（ファイルまたはディレクトリ）を訪れるメソッドです
    def visit(self, entry):
        if isinstance(entry, File):
            # エントリがファイルの場合、そのパスと名前を表示します
            print(f"{self.currentdir}/{entry}")
        elif isinstance(entry, Directory):
            # エントリがディレクトリの場合、そのパスと名前を表示し、その中の全エントリに対して再帰的にvisitを呼び出します
            print(f"{self.currentdir}/{entry}")
            savedir = self.currentdir
            self.currentdir = f"{self.currentdir}/{entry.get_name()}"
            for ent in entry:
                self.visit(ent)
            self.currentdir = savedir

# これはJavaのMainクラスに相当します
def main():
    # ルートディレクトリとその下位ディレクトリ・ファイルを作成します
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

    # ListVisitorを作成し、ルートディレクトリの全エントリを訪れます
    list_visitor = ListVisitor()

    for entry in rootdir:
        list_visitor.visit(entry)

if __name__ == "__main__":
    main()
