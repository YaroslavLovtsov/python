# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.#,

f = open('Exercise5_1.txt', 'w', encoding="utf-8")
input_continue = True
while input_continue:
    curr_string = input('Введите строку или Enter для завершения ввода: ')
    f.writelines(curr_string)
    f.writelines('\n')

    if not curr_string:
        input_continue = False

f.close()


