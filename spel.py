class Player:
    def __init__(self, namn, level, hp ):
        self.namn = namn
        self.level = level
        self.hp = hp

class Monster:
    def __init__(self, typ, hp):
        self.typ = typ
        self.hp = hp

        
    def Skada(self, skada):
        self.skada = skada




player = Player('Hero', 40,358)
player = Player.Skada(100)
monster = Monster('Troll',450)
monster = Monster.Skada(80)
print(player.namn)
