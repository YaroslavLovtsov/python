# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, is_police, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def get_speed(self):
        return self.speed

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if super().get_speed() > 60:
            print(f'Внимание! Скорость автомобиля {self.name} превышена')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if super().get_speed() > 40:
            print(f'Внимание! Скорость автомобиля {self.name} превышена')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

ferrari_512 = SportCar('Ferrari 512', 'red', False, 200)
hyundai_porter = WorkCar('Hyundai Porter', 'blue', False, 35)
volkswagen_polo = TownCar('Volkswagen Polo', 'white', False, 70)
ford_mondeo = PoliceCar('Ford Mondeo', 'black', True, 100)

ferrari_512.go()
volkswagen_polo.go()
ferrari_512.turn('направо')
ford_mondeo.go()
hyundai_porter.go()
ford_mondeo.turn('направо')
ford_mondeo.show_speed()
volkswagen_polo.turn('налево')
hyundai_porter.turn('налево')
volkswagen_polo.show_speed()
ford_mondeo.stop()
volkswagen_polo.turn('налево')
volkswagen_polo.stop()
ferrari_512.show_speed()
ferrari_512.turn('налево')
ford_mondeo.go()
hyundai_porter.show_speed()
hyundai_porter.turn('направо')
ford_mondeo.stop()
ferrari_512.stop()
hyundai_porter.turn('налево')
hyundai_porter.stop()
