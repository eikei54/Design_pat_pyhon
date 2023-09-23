# PrototypeProduct インターフェース（JavaのCloneableに相当）
class PrototypeProduct:
    def use(self, string):
        pass

    def create_clone(self):
        pass

    def __clone__(self):
        pass

# MessageBox クラス
class MessageBox(PrototypeProduct):
    def __init__(self, deco_char):
        self.deco_char = deco_char

    def use(self, string):
        length = len(string.encode())
        print(self.deco_char * (length + 4))
        print(f"{self.deco_char} {string} {self.deco_char}")
        print(self.deco_char * (length + 4))

    def create_clone(self):
        return MessageBox(self.deco_char)

    def __clone__(self):
        return self.create_clone()

# UnderLinepen クラス
class UnderLinepen(PrototypeProduct):
    def __init__(self, ul_char):
        self.ul_char = ul_char

    def use(self, string):
        length = len(string.encode())
        print(string)
        print(self.ul_char * length)

    def create_clone(self):
        return UnderLinepen(self.ul_char)

    def __clone__(self):
        return self.create_clone()

# Manager クラス
class Manager:
    def __init__(self):
        self.showcase = {}

    def register(self, name, prototype):
        self.showcase[name] = prototype

    def create(self, protoname):
        prototype = self.showcase.get(protoname)
        if prototype:
            return prototype.__clone__()
        else:
            return None

# テストコード
def main():
    manager = Manager()
    mbox = MessageBox('*')
    manager.register("mbox", mbox)

    upen = UnderLinepen('_')
    manager.register("upen", upen)

    p1 = manager.create("mbox")
    p1.use("Hello, World!")

    p2 = manager.create("upen")
    p2.use("Python Prototype")

if __name__ == "__main__":
    main()
