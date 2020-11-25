class Car:
    speed = 0
    color = 'white'
    name = 'Volvo'
    is_police = False
    def __init__(self, speed, color, name, is_police = is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Let's go drive!")

    def stop(self):
        print("Let me stop pls!")

    def turn(self, direction):
        print(f"Let's turn us {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Current speed is {self.speed}. Too high speed!")
        else:
            print(f"Current speed is {self.speed}")

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Current speed is {self.speed}. Too high speed!")
        else:
            print(f"Current speed is {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

town_car = TownCar(50, 'Black', 'Lada')
town_car.go()
town_car.show_speed()
town_car.stop()
town_car_2 = TownCar(70, 'Blue', 'Kia')
town_car_2.go()
town_car_2.show_speed()
town_car_2.stop()

work_car = WorkCar(80, 'White', "Mazda")
work_car.go()
work_car.show_speed()
work_car.stop()