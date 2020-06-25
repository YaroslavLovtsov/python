test_number = int(input('Введите целое число: '))
max_digit = -1

while test_number != 0:
    current_digit = test_number % 10
    if current_digit > max_digit:
        max_digit = current_digit
    test_number = test_number // 10

print(max_digit)