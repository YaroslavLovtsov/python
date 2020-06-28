digit = int(input('Введите целое число от 1 до 9: '))

if digit < 0 or digit >= 10:
    print('Ввод некорректен')
else:
    print('n + nn + nnn =', 123 * digit)