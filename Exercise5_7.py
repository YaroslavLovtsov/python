# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

enterprises_dict = {}
average_profit_dict = {}

enterprises_count = 0
total_profit = 0

space = ' '

with open('Exercise5_7.txt', 'r', encoding='utf-8') as f:
    for el in f:
        el_list = el.strip().split(' ')
        len_el_list = len(el_list)
        # Я сделал это задание в предположении, что в списке ве обязательно 4 элемента, потому что
        # название фирмы также может содержать пробелы
        enterprise_name = space.join(el_list[0:len_el_list-2])
        profit_and_loss = list(map(int,el_list[len_el_list - 2:]))
        current_profit_or_loss = profit_and_loss[0] - profit_and_loss[1]
        enterprises_dict[enterprise_name] = current_profit_or_loss
        total_profit += (0 if current_profit_or_loss <= 0 else current_profit_or_loss)
        enterprises_count += 1

average_profit_dict['average_profit'] = total_profit / enterprises_count
json_result = [enterprises_dict, average_profit_dict]
with open("Exercise5_7.json", "w", encoding='utf-8') as write_f:
    json.dump(json_result, write_f)
