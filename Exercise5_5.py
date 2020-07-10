# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#
# В текстовом файле будут не просто какие-то числа, а все простые числа от 1 до 1000000
#
from functools import reduce

def rests(num,list):
    return [num % el for el in list]

def write_to_file():
    eratosfen_list10 = [2,3,5,7]
    eratosfen_list32 = [el for el in range(33) if (el > 1) & ((el in eratosfen_list10) or not(0 in rests(el, eratosfen_list10)))]
    eratosfen_list1000 = [el for el in range(1001) if (el > 1) & ((el in eratosfen_list32) or not(0 in rests(el, eratosfen_list32)))]
    eratosfen_list1000000 = [el for el in range(1000001) if (el > 1) & ((el in eratosfen_list1000) or not(0 in rests(el, eratosfen_list1000)))]

    f_w = open('Exercise5_5.txt','w', encoding='utf-8')
    for el in eratosfen_list1000000:
        f_w.writelines(str(el))
        f_w.writelines(' ')

    f_w.close()

def read_from_file():
    f_r = open('Exercise5_5.txt','r', encoding='utf-8')
    content = f_r.readlines()
    f_r.close()
    return content[0].split(' ')

write_to_file()
my_list = read_from_file()
print(reduce(lambda x,y: (0 if x == '' else int(x)) + (0 if y == '' else int(y)), my_list))


