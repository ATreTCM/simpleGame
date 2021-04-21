""" Участниками являются Компьютер и Игрок. Последовательность ходов определяется
случайным образом. У каждого из игроков одинаковое количество
здоровья и выбор (также случайным образом) следующего из шагов:
1. наносит умеренный урон и имеет небольшой диапазон (18-25)
2. имеет большой диапазон урона (10-35)
3. исцеляет в небольшом диапазоне (в таком же, как и в п.1)
После каждого действия будет напечатано сообщение, которое сообщает
что произошло и сколько здоровья у Игрока и Компьютера. Когда здоровье Компьютера
достигает 35%, увеличивается его шанс на излечение.
Игра завершается, если у одного из участников здоровье достигло 0. """

import random


class Player:
    """Класс определяющий участника игры, имеет параматры здоровье,
    умеренный удар, размашистый удар и действия которые он умеет делать"""

    def __init__(self):
        self.health = 100
        self.damage = [x for x in range(18, 26)]
        self.crit = [x for x in range(10, 36)]
        self.actions = ['hit', 'heal', 'crit_hit']

    def hit(self):  # умеренный урон
        step = random.choice(self.damage)
        self.health = self.health - step
        print('нанес удар ', step)
        return self.health

    def heal(self):  # излечение
        step = random.choice(self.damage)
        self.health = self.health + step
        print('выличился ', step)
        return self.health

    def crit_hit(self):  # размашистый урон
        step = random.choice(self.crit)
        self.health = self.health - step
        print('нанес размашистый удар ', step)
        return self.health


player = Player()  # создаём персонажей
computer = Player()

while True:
    if computer.health <= 35:  # если здоровье Компьютера меньше 35%, увеличиваем шанс излечения
        computer.actions = ['hit', 'heal', 'heal', 'crit_hit']
    else:
        computer.actions = ['hit', 'heal', 'crit_hit']
    if player.health <= 0:  # завершаем программу если здоровье одного из участника ниже или равно 0
        print('Компьютер победил')
        break
    elif computer.health <= 0:
        print('Игрок победил')
        break
    else:
        if random.choice([[], ['g']]):  # слуйный выбор участника, кто будет ходить
            action = random.choice(player.actions)  # случайный выбор действия
            if action == 'hit':
                print('Компьютер', end=' ')
                player.hit()
                if player.health > 0:  # здоровье не может быть ниже 0
                    print('Здоровье Игрока ', player.health)
                else:
                    print('Игрок умер')

            elif action == 'heal':
                print('Компьютер', end=' ')
                computer.heal()
                if computer.health > 100:  # здоровье не может быть больше 100
                    computer.health = 100
                    print('Здоровье Компьютера ', computer.health)
                else:
                    print('Здоровье Компьютера ', computer.health)
            else:
                print('Компьютер', end=' ')
                player.crit_hit()
                if player.health > 0:
                    print('Здоровье Игрока ', player.health)
                else:
                    print('Игрок умер')

        else:
            action = random.choice(computer.actions)
            if action == 'hit':
                print('Игрок', end=' ')
                computer.hit()
                if computer.health > 0:
                    print('Здоровье Компьютера ', computer.health)
                else:
                    print('Компьютер умер')

            elif action == 'heal':
                print('Игрок', end=' ')
                player.heal()
                if player.health > 100:
                    player.health = 100
                    print('Здоровье Игрока ', player.health)
                else:
                    print('Здоровье Игрока ', player.health)
            else:
                print('Игрок', end=' ')
                computer.crit_hit()
                if computer.health > 0:
                    print('Здоровье Компьютера ', computer.health)
                else:
                    print('Компьютер умер')
