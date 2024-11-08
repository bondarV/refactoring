class Bank:
    def __init__(self, balance=0):
        try:
            if balance >= 0:
                self.__balance = balance
            else:
                raise ValueError("Давайте будемо чесними, хто буде відразу з кредитів починати, A? Іншими словами, ви почали історію з банком з від'ємної суми {}".format(balance))
        except ValueError as e:
            print(e)

    def put_money(self, amount):
        if amount < 0:
            raise ValueError("Ви не можете покласти негативну суму")
        self.__balance += amount

    def show_balance(self):
        return self.__balance

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Сума зняття повинна бути більше нуля")
            if self.__balance >= amount:
                self.__balance -= amount
                print("Ви успішно зняли {} грн, на разі на вашому рахунку {} грн".format(amount, self.__balance))
            else:
                raise ValueError("Ви не можете знімати більше аніж у вас доступно на балансі({}), а ви намагаєтесь зняти {}".format(self.__balance, amount))
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    account1 = Bank(1000)
    account1.put_money(100)
    print("Баланс:", account1.show_balance())
    account1.withdraw(1000)
    print("Баланс:", account1.show_balance())
    account1.withdraw(200)  # Приклад з недостатнім балансом
    print("Баланс:", account1.show_balance())
    account2 = Bank(-1000)
