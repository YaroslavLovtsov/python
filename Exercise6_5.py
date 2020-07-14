# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки - ручка {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки - карандаш {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки - маркер {self.title}')

koh_i_noor = Pencil('Koh-i-noor')
koh_i_noor.draw()

paper_clip = Stationery('Paper clip')
paper_clip.draw()
print('Это было', paper_clip.title)

bic = Pen('Bic')
bic.draw()

berlingo = Handle('Berlingo')
berlingo.draw()