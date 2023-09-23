from abc import ABC, abstractmethod


# Cuttable インタフェースの定義
class Cuttable(ABC):
    @abstractmethod
    def cut(self):
        pass


# WoodCutPrint クラスの定義
class WoodCutPrint(ABC):
    @abstractmethod
    def draw(self, hanzai):
        pass

    @abstractmethod
    def cut(self, hanzai):
        pass

    @abstractmethod
    def print(self, hanzai):
        pass

    def create_wood_cut_print(self):
        hanzai = Wood()  # Wood クラスは、Cuttable インタフェースを実装している
        self.draw(hanzai)
        self.cut(hanzai)
        self.print(hanzai)


# TanakasWoodCutPrint クラスの定義
class TanakasWoodCutPrint(WoodCutPrint):
    def draw(self, hanzai):
        print("hanzai にマジックを使って大好きな女の子の絵を描く")

    def cut(self, hanzai):
        print("彫刻刀を使って細部まで丁寧に hanzai を彫る")

    def print(self, hanzai):
        print("版画インクと馬簾を使って豪快にプリントする")


# Wood クラスの定義（Cuttable インタフェースを実装）
class Wood(Cuttable):
    def cut(self):
        pass

# メインプログラム
if __name__ == "__main__":
    tanakas_print = TanakasWoodCutPrint()
    tanakas_print.create_wood_cut_print()
