from abc import ABC, abstractmethod

# Observable: 観察対象オブジェクト
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

# Observer: 観測者
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

# Concrete Observable: 具体的な観察対象オブジェクト
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = None

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

    def get_temperature(self):
        return self._temperature

# Concrete Observer: 具体的な観測者
class Display(Observer):
    def update(self, subject):
        if isinstance(subject, WeatherStation):
            temperature = subject.get_temperature()
            print(f"Temperature is {temperature}°C")

# Client コード
def main():
    weather_station = WeatherStation()
    display1 = Display()
    display2 = Display()

    weather_station.add_observer(display1)
    weather_station.add_observer(display2)

    weather_station.set_temperature(25)  # 25°Cを設定

if __name__ == "__main__":
    main()
