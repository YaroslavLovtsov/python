# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
#

f = open('Exercise5_3.txt', 'r', encoding='utf-8')
f_list = f.readlines()

f_list_count = 0
total_salary = 0

for el in f_list:
    f_list_count += 1
    el_list = el.strip().split(' ')
    salary = float(el_list[1])
    total_salary += salary
    if salary < 20000:
        print(el_list[0],el_list[1])

print('----------------------------------------------------------------')
print('Средняя зарплата:', total_salary / f_list_count)

