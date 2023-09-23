from abc import ABC, abstractmethod

# Product: 銀行口座
class Account(ABC):
    def __init__(self, account_type):
        self.account_type = account_type

    @abstractmethod
    def get_interest_rate(self):
        pass

# Concrete Product 1: 普通預金口座
class SavingAccount(Account):
    def get_interest_rate(self):
        return 0.05

# Concrete Product 2: 当座預金口座
class CheckingAccount(Account):
    def get_interest_rate(self):
        return 0.02

# Creator: 銀行口座を生成するファクトリ
class AccountFactory(ABC):
    @abstractmethod
    def create_account(self):
        pass

# Concrete Creator 1: 普通預金口座のファクトリ
class SavingAccountFactory(AccountFactory):
    def create_account(self):
        return SavingAccount("普通預金口座")

# Concrete Creator 2: 当座預金口座のファクトリ
class CheckingAccountFactory(AccountFactory):
    def create_account(self):
        return CheckingAccount("当座預金口座")

# Client コード
def main():
    saving_account_factory = SavingAccountFactory()
    checking_account_factory = CheckingAccountFactory()

    saving_account = saving_account_factory.create_account()
    checking_account = checking_account_factory.create_account()

    print(f"Interest rate for {saving_account.account_type}: {saving_account.get_interest_rate() * 100}%")
    print(f"Interest rate for {checking_account.account_type}: {checking_account.get_interest_rate() * 100}%")

if __name__ == "__main__":
    main()
