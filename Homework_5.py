class Engine:
    def __init__(self, power):
        self.power = power

    def start_engine(self):
        return f"Engine is started, power: {self.power} H.p."


class Wheels:
    def __init__(self, count):
        self.count = count

    def rotate(self):
        return f"Wheels ({self.count}) spining"


class Electronics:
    def __init__(self, system):
        self.system = system

    def info(self):
        return f"Electric system: {self.system}"


class Car(Engine, Wheels, Electronics):
    def __init__(self, power, count, system, brand):
        Engine.__init__(self, power)
        Wheels.__init__(self, count)
        Electronics.__init__(self, system)
        self.brand = brand

    def full_info(self):
        return (
            f"car: {self.brand}\n"
            f"{self.start_engine()}\n"
            f"{self.rotate()}\n"
            f"{self.info()}"
        )

car = Car(150, 4, "ABS, ESP", "BMW")
print(car.full_info())