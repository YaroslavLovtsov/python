# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
#
f = open('Exercise5_2.txt','r')
f_list = f.readlines()
f_list_count = 0

for el in f_list:
    f_list_count += 1
    el_list = el.strip().split(' ')
    print('Строка', f_list_count, '- в строке', len(el_list), 'слов')

print('----------------------------------------------------------------')
print('Всего в файле', f_list_count, 'строк')
f.close()

