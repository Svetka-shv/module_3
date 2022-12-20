import random

import exceptions
import settings


class EnemyBot:
    def __init__(self):
        self.level = settings.ENEMY_LEVEL
        self.health = self.level

    def decrease_health(self):
        self.health -= 1
        if self.health == 0:
            self.level += 1
            self.health = self.level
            raise exceptions.EnemyDown(self.level - 1)

    def select_attack(self):
        choice_att = random.randint(1, 3)
        return choice_att

    def select_defence(self):
        choice_def = random.randint(1, 3)
        return choice_def


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = settings.INITIAL_PLAYER_HEALTH
        self.score = settings.SCORE

    def decrease_health(self):
        self.health -= 1
        if self.health == 0:
            raise exceptions.GameOver(self.name, self.score)

    def select_attack(self):
        choice = int(input("SELECT ATTACK: WARRIOR(1), ROBBER(2), or WIZARD(3): "))
        return choice

    def select_defence(self):
        choice = int(input("SELECT DEFENCE: WARRIOR(1), ROBBER(2), or WIZARD(3): "))
        return choice

    @staticmethod
    def fight(attack, defence):
        fight_result = 0
        if attack == 1:
            if defence == 1:
                fight_result = 1
            elif defence == 2:
                fight_result = 2
            elif defence == 3:
                fight_result = 3

        if attack == 2:
            if defence == 1:
                fight_result = 2
            elif defence == 2:
                fight_result = 1
            elif defence == 3:
                fight_result = 3

        if attack == 3:
            if defence == 1:
                fight_result = 3
            elif defence == 2:
                fight_result = 2
            elif defence == 3:
                fight_result = 1
        return fight_result

    def attack(self, enemy: EnemyBot) -> None:
        attack = self.select_attack()
        defence = enemy.select_defence()
        fight_result = self.fight(attack, defence)
        if fight_result == 1:
            print("IT'S A DRAW!")
        elif fight_result == 2:
            print("YOUR ATTACK IS FAILED!")
            settings.INITIAL_PLAYER_HEALTH -= 1
        elif fight_result == 3:
            try:
                enemy.decrease_health()
                settings.INITIAL_PLAYER_HEALTH += 1
                print("YOUR ATTACK IS SUCCESSFUL!")
            except exceptions.EnemyDown:
                self.score += 1
                raise

    def defence(self, enemy: EnemyBot):
        defence = self.select_defence()
        attack = enemy.select_attack()
        fight_result = self.fight(defence, attack)
        if fight_result == 1:
            print("IT'S A DRAW!")
        elif fight_result == 2:
            print("ENEMY ATTACK IS FAILED!")
        elif fight_result == 3:
            self.decrease_health()
            print("ENEMY ATTACK IS SUCCESSFUL!")