# Singleton クラス
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Create Instance")
        return cls._instance

# TicketMaker クラス
class TicketMaker:
    _singleton = None

    def __new__(cls):
        if cls._singleton is None:
            cls._singleton = super(TicketMaker, cls).__new__(cls)
            cls._singleton._ticket = 1000
        return cls._singleton

    def getNextTicketNumber(self):
        ticket_number = self._ticket
        self._ticket += 1
        return ticket_number

# Triple クラス
class Triple:
    _instances = {}

    def __new__(cls, id):
        if id not in cls._instances:
            cls._instances[id] = super(Triple, cls).__new__(cls)
            cls._instances[id].id = id
            print(f"Create Instance. id = {id}")
        return cls._instances[id]

    def __str__(self):
        return f"[Triple id = {self.id}]"

# テストコード
def main():
    # Singleton テスト
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # True (同一のインスタンス)

    # TicketMaker テスト
    tm = TicketMaker()
    ticket1 = tm.getNextTicketNumber()
    ticket2 = tm.getNextTicketNumber()
    print(ticket1, ticket2)  # 1000, 1001

    # Triple テスト
    t1 = Triple(0)
    t2 = Triple(1)
    t3 = Triple(2)
    t4 = Triple(0)
    print(t1, t2, t3, t4)  # [Triple id = 0], [Triple id = 1], [Triple id = 2], [Triple id = 0]
    print(t1 is t2, t2 is t3, t3 is t4)  # False, False, True

if __name__ == "__main__":
    main()
