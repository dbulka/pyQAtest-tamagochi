import random

class Tamagochi:
    """
    create pet with some parameters
    """

    def __init__(self, name, max_hp, max_hunger, max_happiness):
        """
        initialize Tamagochi
        :param name: Tamagochi name
        """
        self.name = name
        self.hp = random.randint(0, max_hp)
        self.hunger = random.randint(0, max_hunger)
        self.happiness = random.randint(0, max_happiness)
        self.alive = True

    def is_alive(self, max_happiness, max_hp, max_hunger):
        """
        check Tamagochi alive param
        :return: Tamagochi alive param
        """
        return (0 < self.happiness < max_happiness) and (0 < self.hp < max_hp) and (0 < self.hunger < max_hunger)

    def __str__(self):
        """
        show Tamagochi variables
        """
        return print('hp: {0}| hunger: {1} | happines: {3} | alive: {4}'.format(self.hp, self.hunger, self.happiness,self.alive))
