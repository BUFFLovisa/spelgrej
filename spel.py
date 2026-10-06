class Player:
    def __init__(self, namn, level, attack ):
        self.namn = namn
        self.level = level
        self.attack = attack

class Monster:
    def __init__(self, typ, hp, attack):
        self.typ = typ
        self.hp = hp
        self.attack = attack 

    def Attack(self, attack):
        self.attack = attack
player = Player('Hero', 40,115)


