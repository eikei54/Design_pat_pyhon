
#このコードは、JavaのObserverパターンをPythonに変換したものです。
# Observerパターンは、あるオブジェクト（被験者）の状態が変わったときに、
# そのオブジェクトに依存する他のオブジェクト（観察者）に自動的にその変更を
# 通知するデザインパターンです。
# この例では、NumberGeneratorクラスが被験者として機能し、
# DigitObserverとGraphObserverクラスが観察者として機能します。
# NumberGeneratorは数を生成し、その数が変わるたびに登録されている観察者にその変更を通知します。
# 観察者はそれぞれ異なる方法でその数を表示します。
# このパターンは、あるオブジェクトの状態が他の多くのオブジェクトに
# 影響を与える場合や、それらのオブジェクトがそれぞれ異なる方法で
# その状態の変更に反応する必要がある場合に特に有用です。
# この例では、同じ数が2つの異なる形式（数字とグラフ）
# で表示されます。これは、それぞれが異なる観察者から作成されたためです。
import time
import random
from abc import ABC, abstractmethod

# JavaのインターフェースはPythonの抽象基底クラスに変換します。
class Observer(ABC):
    @abstractmethod
    def update(self, generator):
        pass

class NumberGenerator(ABC):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class DigitObserver(Observer):
    def update(self, generator):
        print(f"DigitObserver: {generator.get_number()}")
        time.sleep(0.1)

class GraphObserver(Observer):
    def update(self, generator):
        print("GraphObserver: " + "*" * generator.get_number())
        time.sleep(0.1)

class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        super().__init__()
        self.number = 0

    def get_number(self):
        return self.number

    def execute(self):
        for _ in range(20):
            self.number = random.randint(0, 50)
            self.notify_observers()

def main():
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()

if __name__ == "__main__":
    main()
