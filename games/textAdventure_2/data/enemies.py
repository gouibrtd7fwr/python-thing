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
    'fl2': Key('Level 2 Key', 2),
    'fl3': Key('Level 3 Key', 3),
}

enemy_pool = [
    Enemy('Snake', 10, 2, 1, 2, 2),
    Enemy('Ghost', 15, 5, 1, 2, 3),
    Enemy('Tank', 50, 1, 1, 3, 7),
]

bosses = {
    'floor_1': Boss('Destroyer of Worlds', 150, 10, 1, 1, 25, "A giant dragon with 3 heads and 4 tails", keys['fl2']),
    'floor_2': Boss('Dungeon Dweller', 250, 25, 2, 2, 40, "A thousand-pound monster which can knock you into the other room.", keys['fl3']),
    'floor_3': Boss('One Damage Man', 1500, 1, 3, 3, 50, "Boss but it only does 1 damage.", keys['fl3']),
}