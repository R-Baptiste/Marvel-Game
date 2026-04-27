""" SKILL CLASSES """

import random
from unit import Unit

class No_Action(Unit) :
    def __init__(self) :
        self.name = "No_Action"
        self.offsets = [
                (0, 0),  # Close diagonals
                ]
        self.attack_power = 0
        self.quantite = 100
        self.distance_attack = 1
        self.chance = 0

class Fists(Unit) :
    def __init__(self) :
        self.name = "Fists"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Close diagonals
                ]
        self.attack_power = 30
        self.quantite = 100
        self.distance_attack = 1
        self.chance = random.uniform(0.5, 1)

class Claws(Unit) :
    def __init__(self):
        self.name = "Claws"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Close diagonals
                (-2, 0), (2, 0), (0, -2), (0, 2) ]
        self.attack_power = 60
        self.quantite = 2
        self.distance_attack = 2
        self.chance = random.uniform(0.5, 1)

class Shield_Throw(Unit) :
    def __init__(self):
        self.name = "Shield_Throw"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1),  # Close diagonals
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, -1), (-2, 1), (2, -1), (2, 1)]
        self.attack_power = 50
        self.quantite = 3
        self.distance_attack = 3
        self.chance = random.uniform(0.5, 1)

class Break_Defenses(Unit) :
    def __init__(self):
        self.name = "Break_Defenses"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Close diagonals
                ]
        self.attack_power = 100
        self.quantite = 1
        self.distance_attack = 1
        self.chance = random.uniform(0.5, 1)     
class Laser(Unit) :
    def __init__(self):
        self.name = "Laser"
        self.offsets = [
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, -1), (2, -1), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1)    # Close diagonals
                ]
        self.attack_power = 100
        self. quantite = 1
        self.distance_attack = 5
        self.chance = random.uniform(0.5, 1)       
class Missile (Unit):
    def __init__(self):
        self.name = "Missile"
        self.offsets = [
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, -1), (2, -1), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Close diagonals
                ]
        self.attack_power = 110
        self.quantite = 1
        self.distance_attack = 5
        self.chance = random.uniform(0.5, 1)
class Block_Opponent (Unit):
    def __init__(self):
        self.name = "Block_Opponent"
        self.offsets = [
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Close diagonals
                ]
        self.temps = 3
        self.attack_power = 40
        self.quantite = 1
        self.distance_attack = 4
        self.chance = random.uniform(0.5, 1)        

class Web_Attack (Unit):
    def __init__(self):
        self.name = "Web_Attack"
        self.offsets = [
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1)  # Close diagonals
                ]
        self.attack_power = 50
        self.quantite = 3
        self.distance_attack = 3
        self.chance = random.uniform(0.5, 1)
class Hammer (Unit):
    def __init__(self):
        self.name = "Hammer"
        self.offsets = [
                (-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Close diagonals
                ]
        self.attack_power = 130
        self.quantite = 1
        self.distance_attack = 5
        self.chance = random.uniform(0.5, 1)        
class Lightning (Unit):
    def __init__(self):
        self.name = "Lightning"
        self.offsets = [
                (-6, 0), (6, 0), (0, -6), (0, 6),
                (-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Close diagonals
                ]
        self.attack_power = 150
        self.quantite = 1
        self.distance_attack = 6
        self.chance = random.uniform(0.5, 1)
class Branch_Attack(Unit) :
    def __init__(self):
        self.name = "Branch_Attack"
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Close diagonals
                ]
        self.attack_power = 40
        self.quantite = 100
        self.distance_attack = 3
        self.chance = random.uniform(0.5, 1)

class Protection (Unit):
    def __init__(self):
        self.name = "Protection"
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Close diagonals
                ]
        self.attack_power = 150
        self.temps = 1
        self.distance_attack = 1
        self.chance = random.uniform(0.5, 1)
        
class Guns(Unit) :
    def __init__(self):
        self.name = "Guns"
        self.offsets = [
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, -2), (-1, 2), (-2, -1), (2, -1)
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1)  # Close diagonals
                ]
        self.attack_power = 120
        self.quantite = 10
        self.distance_attack = 4
        self.chance = random.uniform(0.5, 1)

class Yaka_Arrow(Unit) :
    def __init__(self):
        self.name = "Yaka_Arrow"
        self.offsets = [
                (-3,-3), (-3, 3), (3, -3), (3, 3),
                (-3,-2), (-3, 2), (3, -2), (3, 2),
                (-3, -1), (-3, 1), (3, -1), (3, 1),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, -3), (-2, 3), (2, -3), (2, 3),
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1),
                (-1, -2), (-1, 2), (1, -2), (1, 2),
                (-1, -3), (-1, 3), (1, -3), (1, 3)  # Close diagonals
                ]
        self.attack_power = 100
        self.quantite = 1
        self.distance_attack = 1
        self.chance = random.uniform(0.5, 1)

class Fireball (Unit):
    def __init__(self):
        self.name = "Fireball"
        self.offsets = [(-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, -1), (2, -1), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Close diagonals
                ]
        self.attack_power = 150
        self.quantite = 1
        self.distance_attack = 5
        self.chance = random.uniform(0.5, 1)
      
class Heal (Unit):
    def __init__(self):
        self.name = "Heal"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Close diagonals
                ]
        self.attack_power = 150
        self.quantite = 2
        self.distance_attack = 1
        self.chance = random.uniform(0.5, 1)
        
class Projectile(Unit) :
    def __init__(self):
        self.name = "Projectile"
        self.offsets = [
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonal: left, right, up, down
                (-1, -1), (1, 1), (-1, 1), (1, -1),
                (-1, -2), (-1, 2), (1, -2), (1, 2)  # Close diagonals
                ]
        self.attack_power = 100
        self.quantite = 3
        self.distance_attack = 3
        self.chance = random.uniform(0.5, 1)