# 4. Создать (не программно) текстовый файл со следующим содержимым: 
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
#

my_dict = {'One': 'Один','Two': 'Два','Three': 'Три','Four': 'Четыре'}

f = open('Exercise5_4.txt','r', encoding='utf-8')
f_new = open('Exercise5_4_new.txt','w',encoding='utf-8')

defis = ' — '

pos = 0

f_list = f.readlines()
for el in f_list:
    pos += 1
    el_list = el.strip().split(defis)
    for i,el_str in enumerate(el_list):
        if el_str in  my_dict.keys():
            el_list[i] = my_dict[el_str]

    el_new = defis.join(el_list)
    f_new.writelines(el_new)
    if pos < len(f_list):
        f_new.writelines('\n')

f.close()
f_new.close()

