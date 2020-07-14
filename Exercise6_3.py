# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    def get_full_name(self):
        space = ' '
        return space.join([self.surname, self.name])

    def get_total_income(self):
        return sum(self._income.values())

ivan_petrov = Position('Иван','Иванов','1С-разработчик',{'wage': 120000, 'bonus': 25000})
print(ivan_petrov.get_full_name(), ivan_petrov.get_total_income())
