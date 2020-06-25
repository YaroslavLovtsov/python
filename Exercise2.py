time_in_seconds = int(input('Введите время в секундах: '))

seconds = time_in_seconds % 60
time_in_minutes = time_in_seconds // 60
minutes = time_in_minutes % 60
hours = time_in_minutes // 60

print(f'{hours}:{minutes}:{seconds}')

