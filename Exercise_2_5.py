# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [9, 8, 8, 8, 8, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1]
print('Исходный список')
print(my_list)
left_border = 0
right_border = len(my_list)

try:
    new_value = int(input('Введите новое значение списка: '))
    iter_number = 0

    # Место вставки будем искать с помощью метода бинарного поиска
    # Для того, чтобы понять, в какую позицию вставился у меня результат ввода в случае наличия таких элементов в списке
    # дополнительно выведена позиция вставки
    while True:
        middle_position = (left_border + right_border) // 2

        middle_value = my_list[middle_position]
        if middle_position + 1 == len(my_list):
            print('Место вставки =', middle_position + 1)
            my_list.append(new_value)
            break

        elif (middle_position == 0) & (my_list[middle_position] < new_value):
            print('Место вставки =', 0)
            my_list.insert(0, new_value)
            break

        elif middle_value < new_value:
            right_border = middle_position

        elif (middle_value >= new_value) & (my_list[middle_position + 1] < new_value):
            print('Место вставки =', middle_position + 1)
            my_list.insert(middle_position + 1, new_value)
            break

        else:
            left_border = middle_position

    print('Обработанный список')
    print(my_list)

except ValueError:
    print('Введено некорректноге значение')
