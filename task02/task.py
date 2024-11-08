import random


class Coin:
    def __init__(self, sideup):
        try:
            if sideup == 'heads' or sideup == 'tails':
                self.__sideup = sideup
            else:
                raise ValueError("sideup must be either 'heads' or 'tails'")
        except TypeError as e:
            print(e)

    def toss(self):
        choices = ['heads', 'tails']
        result_of_spin = random.choice(choices)
        if result_of_spin == self.__sideup:
            return 'Вітаю, ви прям щасливчик {}'.format(result_of_spin)
        else:
            return 'Не ваш день {}, а ви обрали {}'.format(result_of_spin, self.__sideup)


if __name__ == "__main__":
    # Введіть heads або tails для випробування везіння
    coin = Coin('heads')
    print(coin.toss())
    coin = Coin('tails')
    print(coin.toss())
    try:
        count_of_iterations = int(input("Введіть кількість підкидань монетки: "))
        if count_of_iterations > 0:
            for _ in range(count_of_iterations):
                print(coin.toss())
        else:
            print("Кількість підкидань повинна бути більше 0.")
    except ValueError:
        print("Будь ласка, введіть коректне число.")
