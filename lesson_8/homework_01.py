"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы: увеличить скорости
(скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0), отображение скорости, задний ход(изменение знака скорости).


"""


class Car:

    def __init__(self, brand: str, model: str, year: int, speed: int=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def speed_view(self):
        print(self.speed)

    def reverse(self):
        self.speed = -self.speed

    def all_info(self):
        print(self.brand, self.model, self.year, self.speed, sep="\n")

if __name__ == '__main__':
    car = Car(brand="BMW", model="E39", year=2000)
    car.all_info()

