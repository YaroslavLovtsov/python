# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def sum_two_max(number1, number2, number3):
    """

    :param number1: целое число
    :param number2: целое число
    :param number3: целое число
    :return: сумма двух наибольших числел
    """
    return number1 + number2 + number3 - min(number1, number2, number3)

arguments = []
for indx in range(3):
    arguments.append(int(input(f'Введите целое число ({indx + 1}): ')))

print('Сумма двух наибольших чисел равна', sum_two_max(arguments[0], arguments[1], arguments[2]))