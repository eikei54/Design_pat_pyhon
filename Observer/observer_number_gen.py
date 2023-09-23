import time
import random

# Observer インターフェースの代わりにメソッドを提供する規約を使用
class Observer:
    def update(self, generator):
        pass

# DigitObserver クラス
class DigitObserver(Observer):
    def update(self, generator):
        print(f"DigitObserver: {generator.get_number()}")
        time.sleep(0.1)

# GraphObserver クラス
class GraphObserver(Observer):
    def update(self, generator):
        count = generator.get_number()
        print("GraphObserver:", "*" * count)
        time.sleep(0.1)

# NumberGenerator クラス
class NumberGenerator:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def execute(self):
        pass

    def get_number(self):
        pass

# RandomNumberGenerator クラス
class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        super().__init__()
        self.number = 0

    def execute(self):
        for _ in range(20):
            self.number = random.randint(0, 49)
            self.notify_observers()

    def get_number(self):
        return self.number

# テストコード
def main():
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()

if __name__ == "__main__":
    main()
