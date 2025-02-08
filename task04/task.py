from abc import ABC, abstractmethod
import random


class Dog(ABC):
    mammal = 'Ссавець'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness = 10

    @property
    @abstractmethod
    def breed(self):
        pass

    @property
    @abstractmethod
    def nature(self):
        pass

    def voice(self):
        pass

    def pet_dog(self):
        self.happiness += random.randint(1, 10)
        print(f"Щастя {self.name} збільшилося до {self.happiness}!")

    def show_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Порода: {self.breed}, Характер: {self.nature}"


class Husky(Dog):
    breed = "хаскі"
    nature = "дружелюбний"

    def voice(self):
        print(f"{self.name} каже: Гав-гав!")

    def howl(self):
        print(f"{self.name} виє: Ууууу!")


class Labrador(Dog):
    breed = "лабрадор"
    nature = "вірний"

    def voice(self):
        print(f"{self.name} каже: Гав-гав!")

    def fetch(self):
        print(f"{self.name} {Dog.nature} приносить м'ячик.")


class Puggy(Dog):
    breed = "мопс"
    nature = "грайливий"

    def voice(self):
        print(f"{self.name} каже: Гав-гав!")

    def turn(self):
        print(f"{self.name} крутиться за хвостом")


class Pets:
    def __init__(self):
        self.dogs = []

    def add_dog(self, pet):
        self.dogs.append(pet)

    def show_pets(self):
        print("Ваші домашні улюбленці:")
        for pet in self.dogs:
            print(pet.show_info())
            pet.voice()
            if isinstance(pet, Husky):
                pet.howl()
            elif isinstance(pet, Labrador):
                pet.fetch()
            elif isinstance(pet, Puggy):
                pet.turn()
            print("-" * 20)


if __name__ == "__main__":
    husky_dog = Husky("Луна", 3)
    labrador_dog = Labrador("Макс", 5)
    puggy_dog = Puggy("Белла", 2)

    print(husky_dog)
    husky_dog.voice()
    husky_dog.howl()
    husky_dog.pet_dog()

    print("\n" + str(labrador_dog))
    labrador_dog.voice()
    labrador_dog.fetch()
    labrador_dog.pet_dog()

    print("\n" + str(puggy_dog))
    puggy_dog.voice()
    puggy_dog.turn()
    puggy_dog.pet_dog()

    my_pets = Pets()
    my_pets.add_dog(husky_dog)
    my_pets.add_dog(labrador_dog)
    my_pets.add_dog(puggy_dog)

    my_pets.show_pets()
