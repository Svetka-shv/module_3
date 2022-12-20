import models
import exceptions


def get_player_name() -> str:
    name: str = ''
    while not name:
        name = input('ENTER YOUR NAME: ').strip()
    return name

def play() -> None:
    player_name = get_player_name()
    player = models.Player(player_name)
    enemy = models.EnemyBot()
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except exceptions.EnemyDown as exc:
            print(exc)
            print(f'Enemy with level {enemy.level - 1} is dead')
            print(f'Player score = {player.score}')
        except exceptions.GameOver as exc:
            print(exc)
            print(f'{player_name} is dead')
            print(f'Score is {player.score}')
            break

if __name__ == '__main__':
    play()