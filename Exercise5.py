earnings = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))

profit_or_loss = earnings - costs

if profit_or_loss <= 0:
    print('Убыток =', -profit_or_loss)
else:
    if earnings != 0:
        print('Рентабельность =', profit_or_loss / earnings)
    else:
        print('Рентабельность = 0')
    stuff_count = int(input('Введите количество сотрудников: '))
    if stuff_count == 0:
        print('Прибыль на одного сотрудника = 0')
    else:
        print('Прибыль на одного сотрудника = ', profit_or_loss / stuff_count)