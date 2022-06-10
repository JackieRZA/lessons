
class Car:
    # def __init__(self, **kwargs):
    #     self.brand = kwargs.get("brand")
    #     self.model = kwargs.get("model")
    #     self.year = kwargs.get("year")
    #     self.speed = kwargs.get("speed", 0)

    def __init__(self, brand: str, model: str, year: int, speed: int = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self) -> None:
        self.speed += 5

    def decrease_speed(self) -> None:
        self.speed -= 5

    def stop(self) -> None:
        self.speed = 0

    def show_speed(self) -> None:
        print(self.speed, "km/s")

    def reverse(self) -> None:
        self.speed *= -1

    def show_all(self):
        print(self.brand, self.model, self.year, self.speed, sep="\n")


if __name__ == '__main__':
    car_1 = Car(brand="VW", model="Passat B3", year=1989)
    car_1.show_all()