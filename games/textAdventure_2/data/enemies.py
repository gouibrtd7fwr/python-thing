class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        # self.armor = armor
        # self.ability = ability
    
enemy_pool = [
    Enemy('Snake', 10, 2),
    Enemy('Ghost', 15, 5),
    Enemy('Tank', 50, 1),
    Enemy('Destroyer of Worlds', 200, 15)
]