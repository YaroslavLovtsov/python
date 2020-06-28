start_distance = float(input("Введите начальную дистанцию: "))
test_distance = float(input("Введите контрольную дистанцию: "))

days = 0
current_distance = start_distance

while True:
    days = days + 1
    if current_distance >= test_distance:
        break
    current_distance = current_distance * 1.1

print(days)


