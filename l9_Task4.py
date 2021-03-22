import random

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("go Car")

    def stop(self):
        print("stop Car")

    def turn(self):
        return(f"turn {random.choice(['left', 'right'])}")

    def show_speed(self):
        self.speed = random.randint(0, 130)
        print(f"Speed {self.speed}")

class TownCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 130)
        if self.speed > 60:
            print(f"Attention! Over speed! {self.speed} km/h")
        else:
            print(f"Speed {self.speed}")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 80)
        if self.speed > 40:
            print(f"Attention! Over speed! {self.speed} km/h")
        else:
            print(f"Speed {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True



a = Car(80,'red','Toyota')
t_car = TownCar(80, 'black', 'Mazda')
w_car = WorkCar(40, 'yellow', 'Kamaz')
s_car = SportCar(200, 'green', 'Ferrari')
p_car = PoliceCar(60, 'white', 'Ford')

print(f"TownCar {t_car.name} {t_car.color}")
t_car.show_speed()
print(f"WorkCar {w_car.name} {w_car.color}")
w_car.show_speed()
print(f"PoliceCar {p_car.name} {p_car.color}")
p_car.show_speed()
p_car.stop()
print(f"SportCar {s_car.name} {s_car.color}")
s_car.turn()
s_car.show_speed()