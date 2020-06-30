# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через
# list и через dict.

jan_tulip = ('Январь', 'зима')
feb_tulip = ('Февраль', 'зима')
mar_tulip = ('Март', 'весна')
apr_tulip = ('Апрель', 'весна')
may_tulip = ('Май', 'весна')
jun_tulip = ('Июнь', 'лето')
jul_tulip = ('Июль', 'лето')
aug_tulip = ('Август', 'лето')
sep_tulip = ('Сентябрь', 'осень')
oct_tulip = ('Октябрь', 'осень')
nov_tulip = ('Ноябрь', 'осень')
dec_tulip = ('Декабрь', 'осень')

month_list = [jan_tulip, feb_tulip, mar_tulip, apr_tulip, may_tulip, jun_tulip, jul_tulip, aug_tulip, sep_tulip, oct_tulip, nov_tulip, dec_tulip]
month_dict = {1: jan_tulip, 2: feb_tulip, 3: mar_tulip, 4: apr_tulip, 5: may_tulip, 6: jun_tulip, 7: jul_tulip, 8: aug_tulip, 9: sep_tulip, 10: oct_tulip, 11: nov_tulip, 12: dec_tulip}
try:
    month_number = int(input('Введите номер месяца (1 - 12): '))

    print('Получено через список:')
    try:
        list_elem = month_list[month_number - 1]
        print(list_elem[0], ',', list_elem[1])
    except IndexError:
        print('Введено не корректное число')

    print('Получено через словарь:')
    try:
        dict_elem = month_dict[month_number]
        print(dict_elem[0], ',', dict_elem[1])
    except KeyError:
        print('Введено не корректное число')

except ValueError:
    stop = True
    print('Введено не целое число')





