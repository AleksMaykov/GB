import random, time
import colorama

class Card:

    def __init__(self):
        pass

    def gen_num(self):
        self.num = random.randrange(1, 91)
        return self.num

    def gen_card(self):
        self.str_card = []
        for num in range (0, 15):
            self.str_card.append(self.gen_num())
        return sorted(self.str_card)

class take_number:

    def __init__(self):
        pass

    def gen_num(self):
        self.num = random.randrange(1, 91)
        return self.num


class Game():

    def __init__(self):
        pass

    def print_card(self, str_card, enemy_card ):
        self.n = 3
        self.str_card = str_card
        self.enemy_card = enemy_card
        print('''Ваша карточка:
          ######################
          {0[0]:<{1}}  {0[3]:<{1}}  {0[6]:<{1}}  {0[9]:<{1}}  {0[12]:<{1}}
          {0[1]:<{1}}  {0[4]:<{1}}  {0[7]:<{1}}  {0[10]:<{1}}  {0[13]:<{1}}
          {0[2]:<{1}}  {0[5]:<{1}}  {0[8]:<{1}}  {0[11]:<{1}}  {0[14]:<{1}}
          ######################
          '''.format(self.str_card, self.n))

        print('''Карточка противника:
          ######################
          {0[0]:<{1}}  {0[3]:<{1}}  {0[6]:<{1}}  {0[9]:<{1}}  {0[12]:<{1}}
          {0[1]:<{1}}  {0[4]:<{1}}  {0[7]:<{1}}  {0[10]:<{1}}  {0[13]:<{1}}
          {0[2]:<{1}}  {0[5]:<{1}}  {0[8]:<{1}}  {0[11]:<{1}}  {0[14]:<{1}}
          ######################
          '''.format(self.enemy_card, self.n))
        time.sleep(1)

    def chek_num(self, card, num):
        self.card = card
        self.num = num
        if self.card.count(self.num) >= 1:
            for _n in self.card[:]:
                if _n == self.num:
                    _count_choose_num = self.card.index(_n)
                    self.card[_count_choose_num] = '*'

        return self.card

    def its_all(self, card,who_card):
        self.card = card
        self.who_card = who_card

        if self.card.count('*') == 15:
                print('''СТОП ИГРА! Одна из карточек полностью заполнена!
и победителем является.........''')
                time.sleep(3)
                print('''{}! Мы поздравляем победителя! И вручаем ему ПРИЗ! 
Вымпел ручной работы и проездной билет \"ТРОЙКА\"'''.format(who_card.upper()))
                time.sleep(3)
                print('Вот номера боченков, сыгравших в этой партии')
                print(last_move)
                time.sleep(3)
                exit()


print('Добрый день. Вас привествует ООО \"Поле Чудес\"')
name = input('Представтесь, пожалуйста: ')
choose = input('Сыграем в ЛОТО? y/n:  ')
move_count = 0
game = Game()

if choose == 'y':
    card = Card()
    str_card = card.gen_card()
    enemy_card = card.gen_card()
    game.print_card(str_card,enemy_card)



    print('Игра началась!')
    time.sleep(2)
    last_move = []
    n = 0

    while n <= 90:
        move = take_number().gen_num()
        if last_move.count(move)==0:
                n += 1
                last_move.append(move)
                print(colorama.Fore.GREEN + 'В игре боченок под номером {}'.format(move))
                print(colorama.Style.RESET_ALL)
                enemy_card = game.chek_num(enemy_card,move)
                game.its_all(enemy_card, 'Компьютерный игрок')

                if str_card.count(move) >= 1:
                    count_choose_num = str_card.index(move)
                    user_choose = input('Зачеркнуть цифру на карточке? y/n:  ')

                    if user_choose == 'y':
                        stt_card = game.chek_num(str_card, move)
                        game.print_card(str_card, enemy_card)
                        game.its_all(str_card, name)
                    else:
                        print(colorama.Fore.RED + 'Вы передумали играть? Жаль, очень жаль. Всего доброго {}'.format(name.capitalize()))
                        print(colorama.Style.RESET_ALL)
                        exit()
    else:
        print(colorama.Fore.RED + 'Мы сожалеем но в данной партии нет победителя и очень ценный приз будет перенесет в будущую партию')
        print(colorama.Style.RESET_ALL)
        exit()

else:
    print(colorama.Fore.RED + 'Ну.... наше дело предложить, ваше дело - сбежать с поля боя.')
    print(colorama.Style.RESET_ALL)
    exit()
