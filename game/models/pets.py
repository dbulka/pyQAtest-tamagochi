import random
from pyQAtest_tamagochi.game.models.pet import Tamagochi


class Dog(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'Dog')
        self.hp = random.randint(0,100)
        self.hunger = random.randint(0,50)
        self.happiness = random.randint(0,200)
        self.alive = True

    def __str__(self):
        return self.name

class Robot(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'Robot')
        self.hp = random.randint(0,200)
        self.hunger = random.randint(0,300)
        self.happiness = random.randint(0,50)
        self.alive = True

    def __str__(self):
        return self.name

class Python(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'Python')
        self.hp = random.randint(0,50)
        self.hunger = random.randint(0,200)
        self.happiness = random.randint(0,50)
        self.alive = True

    def __str__(self):
        return self.name

class MickyMouse(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'MickyMouse')
        self.hp = random.randint(0,100)
        self.hunger = random.randint(0,100)
        self.happiness = random.randint(0,100)
        self.alive = True

    def __str__(self):
        return self.name

class Cheburashka(Tamagochi):

    def __init__(self):
        Tamagochi.__init__(self,'Cheburashka')
        self.hp = random.randint(0,150)
        self.hunger = random.randint(0,100)
        self.happiness = random.randint(0,150)
        self.alive = True

    def __str__(self):
        return self.name



