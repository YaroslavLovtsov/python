# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def user_info(name, surname, birth_year, city, e_mail, phone_number):
    """

    :param name: Имя пользователя
    :param surname: Фамилия полльзователя
    :param birth_year: Год рождения пользователя
    :param city: Город проживания пользователя
    :param e_mail: E-mail пользователя
    :param phone_number: Номер телефона пользователя

    :return: Строка информации о пользователе

    """
    space = ': '
    comma_space = ', '
    result = []
    result.append(space.join(['Имя', name]))
    result.append(space.join(['Фамилия', surname]))
    result.append(space.join(['Год рождения', birth_year]))
    result.append(space.join(['Город проживания', city]))
    result.append(space.join(['E-mail', e_mail]))
    result.append(space.join(['Телефон', phone_number]))

    return comma_space.join(result)

param_dict = {'имя': '', 'фамилию': '', 'год рождения': '', 'город проживания': '', 'e-mail': '', 'телефон': ''}

for indx in param_dict.keys():
    user_data = input(f'Введите {indx}: ')
    param_dict[indx] = user_data

# В реальности, конечно лучше было не делить словарь, а обрабатывать именно словарь
# Но таково задание

print(user_info(name = param_dict['имя'], surname = param_dict['фамилию'], birth_year = param_dict['год рождения'],
                city = param_dict['город проживания'], e_mail = param_dict['e-mail'], phone_number = param_dict['телефон']))
