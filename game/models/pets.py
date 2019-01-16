import random
from pyQAtest_tamagochi.game.models.pet import Tamagochi


class Dog(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self, 'Dog', max_happiness = 200, max_hunger = 50, max_hp = 100)

    def __str__(self):
        return self.name

    def is_alive(self):
        Tamagochi.is_alive(self, max_happiness = 200, max_hunger = 50, max_hp = 100)


class Robot(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'Robot', max_happiness = 50, max_hunger = 300, max_hp = 200)

    def __str__(self):
        return self.name

    def is_alive(self):
        Tamagochi.is_alive(self, max_happiness = 50, max_hunger = 300, max_hp = 200)


class Python(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'Python', max_happiness = 50, max_hunger = 200, max_hp = 50)

    def __str__(self):
        return self.name

    def is_alive(self):
        Tamagochi.is_alive(self, max_happiness = 50, max_hunger = 200, max_hp = 50)

class MickyMouse(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'MickyMouse', max_happiness = 100, max_hunger = 100, max_hp = 100)

    def __str__(self):
        return self.name

    def is_alive(self):
        Tamagochi.is_alive(self, max_happiness = 100, max_hunger = 100, max_hp = 100)

class Cheburashka(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'Cheburashka', max_happiness = 150, max_hunger = 100, max_hp = 150)

    def __str__(self):
        return self.name

    def is_alive(self):
        Tamagochi.is_alive(self, max_happiness = 150, max_hunger = 100, max_hp = 150)



