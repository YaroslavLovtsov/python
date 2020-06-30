# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

one_more_value = True
test_list = []

while one_more_value:
    new_value = input('введите значение или нажмите Enter для окончания ввода: ')
    if new_value == "":
        one_more_value = False
    else:
        test_list.append(new_value)

print('Исходный список:')
print(test_list)
#
test_list_length = len(test_list)
#
if test_list_length:
    for indx in range(test_list_length // 2):
        temp_val = test_list[2*indx+1]
        test_list[2 * indx + 1] = test_list[2*indx]
        test_list[2 * indx] = temp_val
#
print('Обработанный список:')
print(test_list)

