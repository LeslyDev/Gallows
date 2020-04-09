import random


class Game:
    def __init__(self):
        self.list_of_word = ['skillfactory', 'testing', 'blackbox', 'pytest',
                             'unittest', 'coverage']
        self.game_status = False
        self.possible_points = 4
        print('Вы хотите начать игру?')
        self.current_word = random.choice(self.list_of_word)
        self.word = '_ ' * len(self.current_word)

    @staticmethod
    def find_indexes(string: str, letter):
        count = 0
        start = 0
        list_indexes = []
        for i in string:
            if i == letter:
                count += 1
        for i in range(count):
            b = string.find(letter, start, len(string) - 1)
            list_indexes.append(b)
            start = b + 1
        if list_indexes[count - 1] == -1:
            list_indexes[count - 1] = len(string) - 1
        return list_indexes

    def foo(self, a):
        if (a.isalpha()) and (len(a) == 1) and (a in self.current_word):
            temp = self.word.split()
            list_of_index = self.find_indexes(self.current_word, a)
            for i in list_of_index:
                temp[i] = a
            self.word = ' '.join(temp)
            print(self.word)
            if '_' not in self.word:
                print('Поздравляю вы победили!')
                self.game_status = False
                return 'Победа'
            return 'Буква угадана'
        else:
            print('Такой буквы нет!')
            print(self.word)
            self.possible_points -= 1
            if self.possible_points == 0:
                print('Вы проиграли!')
                self.game_status = False
                return 'Вы проиграли'
            return 'Такой буквы нет'

    def game(self):
        while self.game_status:
            print('У вас есть {} права на ошибку'.format(self.possible_points))
            print('Введите букву')
            a = input()
            self.foo(a)

    def start(self):
        if input().lower() == 'да':
            self.game_status = True
            print(self.word)
            self.game()
        else:
            self.game_status = False


a = Game()
if __name__ == '__main__':
    a.start()
