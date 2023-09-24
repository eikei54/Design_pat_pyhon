# このコードは、JavaのPrototypeパターンをPythonに変換したものです。
# Prototypeパターンは、新しいオブジェクトを作成するために
# 既存のオブジェクトを複製するデザインパターンです。
# このパターンは、オブジェクトの作成コストが高い場合や、
# クラスから直接オブジェクトを作成することが困難な場合に特に有用です。
# この例では、Productクラスがプロトタイプとして機能し、Managerクラスが
# それを使用して新しいオブジェクトを作成します。具体的なプロトタイプはM
# essageBoxとUnderlinePenで、それぞれ異なる方法で文字列を表示します。
# これらのオブジェクトは、それぞれ異なる名前でManagerに登録され、
# 後でその名前を使用して複製されます。このようにして、プログラムは実行時に
# 新しいオブジェクトを動的に生成できます。このパターンは、柔軟性と再利用性を提供し、
# 大規模なソフトウェアシステムでは頻繁に使用されます。
# この例では、メッセージボックスと下線ペンが異なる方法で
# 同じメッセージ（“Hello, world.”）を表示します。
# これは、それぞれが異なるプロトタイプから作成されたためです。


# JavaのクラスはPythonのクラスに変換します。
class Product:
    def use(self, s):
        pass

    def create_copy(self):
        pass

# JavaのインターフェースはPythonの抽象基底クラスに変換します。
class Manager:
    def __init__(self):
        self.showcase = {}

    def register(self, name, proto):
        self.showcase[name] = proto

    def create(self, protoname):
        p = self.showcase[protoname]
        return p.create_copy()

class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, s):
        decolen = 1 + len(s) + 1
        print(self.decochar * decolen)
        print(self.decochar + s + self.decochar)
        print(self.decochar * decolen)

    def create_copy(self):
        return MessageBox(self.decochar)

class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, s):
        ulen = len(s)
        print(s)
        print(self.ulchar * ulen)

    def create_copy(self):
        return UnderlinePen(self.ulchar)

# メイン関数
def main():
    # 準備
    manager = Manager()
    upen = UnderlinePen('-')
    mbox = MessageBox('*')
    sbox = MessageBox('/')

    # 登録
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)

    # 生成と使用
    p1 = manager.create("strong message")
    p1.use("Hello, world.")

    p2 = manager.create("warning box")
    p2.use("Hello, world.")

    p3 = manager.create("slash box")
    p3.use("Hello, world.")

if __name__ == "__main__":
    main()
