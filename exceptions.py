class EnemyDown(Exception):
    def __str__(self):
        return 'Enemy down'


class GameOver(Exception):
    def __str__(self):
        return 'Game over'