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
    def __init__(self, name, enemy):
        self.name = name
        self.enemy = enemy
        self.health = 100

    def hit(self):
        step = random.choice(range(18, 26))
        self.health -= step
        return self.health, 'нанес удар', step, self.enemy, self.name

    def heal(self):
        step = random.choice(range(18, 26))
        self.health += step
        return self.health, 'выличился', step, self.name, self.name

    def crit_hit(self):
        step = random.choice(range(10, 36))
        self.health -= step
        return self.health, 'нанес размашистый удар', step, self.enemy, self.name

def play(player1, player2):
    while player1.health > 0 and player2.health > 0:
        players = [player1, player2]
        player_action = random.choice(players).action()
        print("{} {} {} {}\nЗдоровье {}а {}".format(player_action[3], player_action[1], player_action[2], player_action[4],
                                                    player_action[4], player_action[0]))
    return "{} победил".format(player1.name if player2.health <= 0 else player2.name)

if __name__ == "__main__":
    player = Player('Игрок', 'Компьютер')
    computer = Player('Компьютер', 'Игрок')
    print(play(player, computer))
