from random import randint
from time import sleep

class Card:
    def __init__(self):
        distrib_list = [0 for el in range(9)]
        self.card = [[None for el1 in range(9)] for el2 in range(3)]
        used_numbers = []
        self.numbers_remains = 15
        self.is_line = False
        self.is_bingo = False
        self.check_line = True

        for i in range(3):
            current_used_numbers = []
            while len(current_used_numbers) < 5:
                new_number = int(randint(1,90))
                if not new_number in used_numbers:
                    if new_number < 10:
                        index = 0
                    elif new_number == 90:
                        index = 8
                    else:
                        index = new_number // 10
                    try:
                        if (i == 2) & (0 in distrib_list) & (distrib_list[index] != 0):
                            pass
                        elif self.card[i][index] == None:
                            self.card[i][index] = new_number
                            used_numbers.append(new_number)
                            current_used_numbers.append(new_number)
                            distrib_list[index] += 1
                    except IndexError:
                        print(distrib_list)
                        print(index)

    def del_number(self, number, to_delete, to_check):
        number_is_found = False
        mistake = False

        for i in range(3):

            line_is_empty = True

            for j in range(9):
                if self.card[i][j] == number:
                    if to_check != to_delete:
                        mistake = to_check

                    self.card[i][j] = '--'
                    number_is_found = True
                    self.numbers_remains -= 1

                if (self.card[i][j] != None) & (self.card[i][j] != '--'):
                    line_is_empty = False

            if line_is_empty & self.check_line:
                self.is_line = True

        if to_delete & to_check & (not number_is_found):
            mistake = True

        if self.numbers_remains == 0:
            self.is_bingo = True

        return mistake

    def __str__(self):
        s = '-' * 46 +'\n'
        for i in range(3):
            s += '|' + '|'.join(['    ' if self.card[i][j] == None else (' -- ' if self.card[i][j] == '--' else (' '+(str(self.card[i][j]) if self.card[i][j] >= 10 else ' '+str(self.card[i][j]))+' ')) for j in range(9)]) + '|\n'
            s += '-' * 46 + '\n'
        return s

class Sack:
    def __init__(self):
        self.sack = [1 + el for el in range(90)]
        for i in range(90):
            ind_a = randint(1, 90)
            temp = self.sack[ind_a - 1]
            self.sack[ind_a - 1] = self.sack[i]
            self.sack[i] = temp

    def new_keg(self):
        return self.sack.pop()


class Game:
    def __init__(self):
        self.computer_card = Card()
        print(self.computer_card)
        self.my_card = Card()
        print(self.my_card)

        self.move = 0
        self.game_over = False

        self.sack = Sack()
        self.check_lines = True

    def start(self):


        while (not self.game_over):

            keg = self.sack.new_keg()
            self.move += 1
            print('Выпавший бочонок:',keg,"(Осталось",len(self.sack.sack),"бочонков)")

            to_delete = False if input('Удалить? 0 - нет, иначе - да ') == '0' else True

            self.computer_card.del_number(keg, True, False)
            print(f'Карточка компьютера (осталось номеров {self.computer_card.numbers_remains}):')
            print(self.computer_card)

            mistake = self.my_card.del_number(keg, to_delete, True)
            print(f'Ваша карточка (осталось номеров ',self.my_card.numbers_remains,'):')
            print(self.my_card)

            if mistake:
                print('Ошибка. Вы проиграли')
                self.game_over = True
                continue

            if self.check_lines & (self.computer_card.is_line | self.my_card.is_line):
                if self.computer_card.is_line & self.my_card.is_line:
                    print(f'Линия! Оба игрока победили на {self.move} ходу')
                elif self.computer_card.is_line:
                    print(f'Линия! Компьютер победил на {self.move} ходу')
                else:
                    print(f'Линия! Вы победили на {self.move} ходу')
                sleep(5)
                self.check_lines = False
                self.computer_card.check_line = False
                self.my_card.check_line = False

            if (self.computer_card.is_bingo | self.my_card.is_bingo):
                self.game_over = True
                if self.computer_card.is_bingo & self.my_card.is_bingo:
                    print(f'Бинго! Оба игрока победили на {self.move} ходу')
                elif self.computer_card.is_bingo:
                    print(f'Бинго! Компьютер победил на {self.move} ходу')
                else:
                    print(f'Бинго! Вы победили на {self.move} ходу')

                print('В мешке осталось:')
                print(', '.join(list(map(str, self.sack.sack))))

new_game = Game()
new_game.start()

