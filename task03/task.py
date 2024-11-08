class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        if speed >= 0:
            self.speed = speed
        else:
            raise ValueError('Speed must be non-negative')

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            print('Stop pushing your breaks,you already stopped the car')
            self.speed = 0

    def get_speed(self):
        return self.speed

def add_speed(car, count):
    for _ in range(count):
        car.accelerate()
        print(f"Поточна швидкість нашого автомобіля на відрізку: {car.get_speed()} км/год")

def reduce_speed(car, count):
    for _ in range(count):
        car.brake()
        print(f"Поточна швидкість нашого автомобіля на відрізку: {car.get_speed()} км/год")

if __name__ == '__main__':
    leaf = Car("Хонда", "2-311", 2022, 10)

    print("Прискорення автомобіля:")
    add_speed(leaf, 5)

    print("Гальмування автомобіля:")
    reduce_speed(leaf, 5)
    reduce_speed(leaf, 3)