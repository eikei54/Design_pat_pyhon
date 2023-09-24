#以下は、指定されたJavaコードをPythonに変換したものです。
# このコードは、シングルトンパターンを実装しています。
# シングルトンパターンは、特定のクラスのインスタンスが
# 1つしか存在しないことを保証するデザインパターンです。

class Singleton:
    # _singletonはクラス変数で、Singletonクラスの唯一のインスタンスを保持します
    _singleton = None

    @staticmethod
    def getInstance():
        # インスタンスがまだ存在しない場合は生成します
        if not Singleton._singleton:
            Singleton._singleton = Singleton()
            print("インスタンスを生成しました。")
        # 既存のインスタンスを返します
        return Singleton._singleton

def main():
    print("Start.")
    obj1 = Singleton.getInstance()
    obj2 = Singleton.getInstance()
    # obj1とobj2が同じインスタンスであることを確認します
    if obj1 == obj2:
        print("obj1とobj2は同じインスタンスです。")
    else:
        print("obj1とobj2は同じインスタンスではありません。")
    print("End.")

if __name__ == "__main__":
    main()
