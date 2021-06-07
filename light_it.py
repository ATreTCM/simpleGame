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


from random import choice


class Player:
    """Класс определяющий игрока, имеет параматры здоровье,
    умеренный удар, размашистый удар и действия которые он умеет делать"""

    def __init__(self):
        self.name = 'Игрок'
        self.enemy = 'Компьтер'
        self.health = 100
        self.damage = [x for x in range(18, 26)]
        self.crit = [x for x in range(10, 36)]

    def hit(self):  # умеренный урон
        step = choice(self.damage)
        self.health = self.health - step
        return self.health, 'нанес удар', step, self.enemy, self.name

    def heal(self):  # излечение
        step = choice(self.damage)
        self.health = self.health + step
        return self.health, 'выличился', step, self.name, self.name

    def crit_hit(self):  # размашистый урон
        step = choice(self.crit)
        self.health = self.health - step
        return self.health, 'нанес размашистый удар', step, self.enemy, self.name
        
    def action(self): # случай выбор действий
        act = [self.heal, self.crit_hit, self.hit]
        return choice(act)()
        
class Computer(Player):
    """Класс компьтера, наследует класс игрока, но со своими особенностями"""
    
    def __init__(self):
        Player.__init__(self)
        self.name, self.enemy = self.enemy, self.name
    
    def action(self):
        if self.health<=35: # если здоровье компьтера меньше 35 он чаще лечится
            print('Компьтер стал сильнее')
            act = [self.heal, self.crit_hit, self.hit, self.heal]
            return choice(act)()
        else:
            act = [self.heal, self.crit_hit, self.hit]
            return choice(act)()

player = Player()  # создаём персонажей
computer = Computer()

def play(player1, player2):   #функция самой игры
    fu = [player1.action, player2.action]
    g = choice(fu)() #случайный ход копьютер или игрок
    print(g[3], g[1], g[2],'\n','Здоровье', g[4]+'а', g[0])
    if int(g[0]) > 0:
        return play(player1, player2) #если все живы, продолжаем
    else:
        if player1.health<=0:
            return 'Компьтер победил'
        else:
            return 'Игрок победил'

print(play(player, computer))



             