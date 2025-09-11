from data.items import Key

class Enemy:
    def __init__(self, name, health, damage, level_min, level_max, coin_amt):
        self.name = name
        self.health = health
        self.damage = damage
        self.level_min = level_min
        self.level_max = level_max
        self.coin_amt = coin_amt
        # self.armor = armor
        # self.ability = ability

class Boss(Enemy):
    def __init__(self, name, health, damage, level_min, level_max, coin_amt, description, drop_key):
        super().__init__(name, health, damage, level_min, level_max, coin_amt)
        self.description = description
        self.drop_key = drop_key
        # self.armor = armor
        # self.ability = ability
keys = {
    'fl1': Key('Level 1 Key', 1),
}

enemy_pool = [
    Enemy('Snake', 10, 2, 1, 2, 2),
    Enemy('Ghost', 15, 5, 1, 2, 3),
    Enemy('Tank', 50, 1, 1, 3, 7),
]

bosses = {
    'floor_1': Boss('Destroyer of Worlds', 200, 15, 1, 1, 25, "A giant dragon with 3 heads and 4 tails", keys['fl1']),
}