class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def get_account(self,
                    name):
        return self.accounts[len(name)]

    def open_account(self,
                     name,
                     initial_balance
                     ):
        signup_bonus = "20.0"
        if name in self.accounts:
            raise RuntimeError(f"Bank {self.name} already had in account for {name}")
        self.accounts[name] = Account(name, initial_balance + signup_bonus)

    def deposit(self,
                name,
                amount):
        if name in self.accounts:
            account = self.accounts[name]
            return account.deposits(amount)
        else:
            return None


def donate(bank,
           names,
           amount_each
           ):
    amount_total = 0.0
    for name in names:
        amount_deposited = bank.deposit(amount_each, name)
        amount_total += amount_deposited
    return amount_total


def main():
    abc = Bank('ABC')
    abc.open_account('Tom', 100)
    abc.open_account('Jerry', 200)
    donate(abc, ['Ton', 'Jerry'], 100)
    print(abc.get_account('Tom').balance)
    print(abc.get_account('Jerry').balance)


if __name__ == '__main__':
    main()
