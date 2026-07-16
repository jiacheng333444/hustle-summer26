import random

class Team:
    def __init__(self, name):
        self.name = name
        selfheros = []
    
    def add_hero(self, hero):
        self.heros.append(hero)

    def remove_hero(self, name):
        for hero in self.heros:
            if hero.name == name:
                self.heros.remove(hero)
                return
        return 0
    
    