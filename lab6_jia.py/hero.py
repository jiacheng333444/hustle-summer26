import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0
    
    

    def battle(self, opponent):
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return
        
        print(f"BATTLE START: {self.name} vs {opponent.name}!")

        while self.current_health > 0 and opponent.current_health > 0:

            my_damage = self.attack()
            opponent.take_damage(my_damage)

            opponent_damage = opponent.attack()
            self.take_damage(opponent_damage)

            print(f"{self.name} HP: {self.current_health} | {opponent.name} HP: {opponent.current_health}")
            print("-" * 30)

        if self.current_health <= 0 and opponent.current_health <= 0:
            print("Both died fr fr")
            self.add_death(1)
            opponent.add_death(1)
        elif self.current_health <= 0:
            print(f"{opponent.name} won fr")
            opponent.add_kill(1)
            self.add_death(1)
        else:
            print(f"{self.name} won fr")
            self.add_kill(1)
            opponent.add_death(1)

    def add_kill(self, num_kills):
        self.kills +=  num_kills
    
    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        print(total_damage)
        return(total_damage)

    def add_armor(self, armor):
        self.armors.append(armor)

    def block(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        print(total_defense)
        return(total_defense)

    def take_damage(self, damage):
        blocked = self.block()
        damage_taken = max(damage - blocked, 0)
        self.current_health -= damage_taken
        if self.current_health < 0:
            self.current_health = 0
        return damage_taken






if __name__ == "__main__":
    my_hero = Hero("Hatsune-Miku", 150)
    my_opponent = Hero("Kasane-Teto", 270)
    
    my_hero.add_ability(Ability("Hatsune-Miku Does Not Talk to British People!", 75))
    my_hero.add_ability(Ability("Leek-Strike", 60))
    my_hero.add_ability(Ability("Miku-Dayo", 33))
    leek_sword = Weapon("Leek-Sword", 50)
    my_hero.add_ability(leek_sword)
    my_hero.add_armor(Armor("Pig-tails", 18))
    my_hero.add_armor(Armor("Shield-Of-Leek", 20))

    my_opponent.add_ability(Ability("Teto-Territory", 45))
    my_opponent.add_ability(Ability("Baguette-Strike", 25))
    my_opponent.add_armor(Armor("Drill-Hair-Shield", 12))
    baguette_launcher = Weapon("Baugette-Launcher", 60)
    my_opponent.add_ability(baguette_launcher)
    my_opponent.add_armor(Armor("Baguette-Parry", 30))

    my_hero.battle(my_opponent)
    # my opponents damage is unbalanced im nerfing her and shes still winning
    
    



