class Character(object):
    
    def __init__(self, health, power):
        self.health = health
        self.power = power
        print(health, power)
   
    def alive(self):
        if self.health > 0:
            return True
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s does %d damage to %s." % (self, self.power, enemy)) 

    def print_status(self, enemy):
        print("The enemy has %d health and %d power." % (enemy.health, enemy.power))
