import random


class Player:
    '''
    name = Имя игрока
    bull = Номер выстрела в барабане(6 слотов под пулю), после которого игрок умрёт
    use_bull = Номер текущего выстрела, после проверки выстрела и его вывода добавляется 1
    '''

    def __init__(self, name):
        self.name = name
        self.bull = 1
        self.use_bull = 1


class Game:
    def __init__(self):
        self.size_vins = {}

    def turn_game(self, players):
        '''
        players: {int: Player()}
        '''
        next_str = '\n'
        str_players = f'{next_str}{next_str.join(f"{i} - {players[i].name}" for i in players.keys())}'
        for i in range(len(players) * 6):
            print(f'Стол - {self.get_value_card()}')
            player = input(f'''Какой игрок проиграл? {str_players}\n''')
            while player not in players.keys():
                print('Такого игрока уже нет за столом!')
                player = input(f'''Какой игрок проиграл?
                {str_players}''')
            value_bullet = players[player].use_bull
            if players[player] and players[player].bull != players[player].use_bull:
                print('Продолжаем, игрок - жив')
                print('*******************')
                print(f'Игрок {players[player].name} совершил: {value_bullet} выстрелов')
                print('*******************')
                players[player].use_bull += 1
            elif players[player] and players[player].bull == players[player].use_bull:
                print(f'Игрок {players[player].name} мёртв!')
                if len(players) <= 2:
                    players.pop(player)
                    name_vin = list(players.values())[0].name
                    print(f'Победил - {name_vin}')
                    if player_vin := self.size_vins[name_vin]:
                        player_vin += 1
                    else:
                        self.size_vins[name_vin] = 1
                    return self.end_game()
                else:
                    players.pop(player)
                    print(f'Играем дальше ^V^')
                    print(f'Живые игроки: {", ".join(i.name for i in list(players.values()))}')
                    self.turn_game(players)
                    return False
            else:
                print('Ты всё сломал! Стреляй сново в кого хотел!')

    def get_value_card(self):
        card = ['J', 'Q', 'K', 'A']
        return random.choice(card)

    def end_game(self, question='Хотите сыграть ещё?', answers='1 - Да, 2 - Нет') -> bool:
        print(question)
        print(answers)
        if int(input('Введите ваш ответ')) == 2:
            print('До свидания!')
            print(f'''Счёт сессии: {self.size_vins}''')
            input('Нажмите любую клавишу')
            exit()
        else:
            print('Продолжаем!')
            for i in range(100):
                print()
            return False


def main():
    is_game = True
    game = Game()
    while is_game:
        num_players = int(input('Сколько игроков будет за столом?\n'))
        if num_players > 1 and num_players <= 4:
            all_players = [Player(name=input(f'Введите имя {i} игрока: ')) for i in range(num_players)]
            break
        else:
            is_game = game.end_game(question='Не верное кол-во игроков!', answers='''
1 - Продолжить игру
2 - Закончить игру''')

    while is_game:
        players = {}
        for i in range(len(all_players)):
            players[str(i)] = all_players[i]
            if len(game.size_vins) != len(all_players):
                game.size_vins[players[str(i)].name] = 0
            players[str(i)].bull = random.randint(1, 6)
            players[str(i)].use_bull = 1
        if game.turn_game(players):
            is_game = False


main()
