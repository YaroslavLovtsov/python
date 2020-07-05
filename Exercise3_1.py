# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_divide(numerator, denominator):
    """
    :param numerator: Вещественное число, делимое 
    :param denominator: Вещественное число, делитель
    :return: Частное от деления
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 'Ошибка: деление на 0'


numerator = input('Введите делимое: ')
denominator = input('Введите делитель: ')

try:
    print(my_divide(float(numerator), float(denominator)))
except ValueError:
    print('Введенные значения некорректны')

