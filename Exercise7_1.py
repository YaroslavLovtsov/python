# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix_list):
        self._height = len(matrix_list)
        self._width = len(matrix_list[0])
        max_el = max(matrix_list[0])
        min_el = min(matrix_list[0])
        for el in matrix_list[1:]:
            if len(el) != self._width:
                raise 'MatrixSizeError'
            current_max_el = max(el)
            current_min_el = min(el)
            if current_max_el > max_el:
                max_el = current_max_el
            if current_min_el < min_el:
                max_el = current_min_el
        self._max_el = max_el
        self._min_el = min_el
        self.matrix_list = matrix_list

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def format_elem(self, elem):
        empty_str = ''
        new_len = max(len(str(self._max_el)),len(str(self._min_el)))
        cur_elem_str = str(elem)
        return empty_str.join([' ' if new_len - len(cur_elem_str) > el else  cur_elem_str[el - (new_len - len(cur_elem_str))] for el in range(new_len)])

    def __str__(self):
        space = ' '
        new_line = '\n'

        result_list = []
        for row in self.matrix_list:
            result_list.append(space.join([self.format_elem(col) for col in row]))

        return new_line.join(result_list)

    def __add__(self, other):
        result = []
        if other.get_width() != self._width:
           raise 'AddingMatricesDiffSize'

        if other.get_height() != self._height:
            raise 'AddingMatricesDiffSize'

        for row in range(self._height):
            result.append(list(self.matrix_list[row][col] + other.matrix_list[row][col] for col in range(self._width)))
        return Matrix(result)

try:
    my_matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
except NameError:
    print('Структура матрицы my_matrix1 некорректна')

try:
    my_matrix2 = Matrix([[77, 888], [9999, 10101], [222222, 3333333]])
except TypeError:
    print('Структура матрицы my_matrix2 некорректна')

try:
    print(my_matrix1 + my_matrix2)
except TypeError:
    print('Размеры матриц не совпадают')
except NameError:
    print('Сумма матриц не может быть вычислена')
