import logging
from pyQAtest_tamagochi.game.views.interface import GameInterface
from pyQAtest_tamagochi.game.models import Tamagochi, random, pets


class User(GameInterface):
    """
    part of interface, which cooperates with user
    """

    def give_food(self, pet):
        """
        change Tamagochi hunger value
        :hunger pet: Tamagochi hunger
        :return: deduct input value from Tamagochi hunger
        """
        pet.hunger -= int(input('enter amount of food: '))

    def give_hp(self,pet):
        """
        change Tamagochi hp value
        :hp pet: Tamagochi hp
        :return: deduct input value from Tamagochi hp
        """
        pet.hp  += int(input('enter amount of happiness: '))

    def play(self,pet):
        """
        change Tamagochi happiness value
        :happiness pet: Tamagochi happiness
        :return: deduct input value from Tamagochi happiness
        """
        pet.happiness  += int(input('enter amount of hp: '))

    def make_choice(self, n):
        """
        give to user ways to control Tamagochi
        :param n: step number
        :return: number of way
        """
        print("""
        Choose way:
        #1 - Feed pet
        #2 - Heal pet
        #3 - Play with pet
              """)
        condition = ('1','2','3')
        resp = True
        while resp:
            choice = self.ask_question('Enter number of way: ')
            if choice in condition:
                resp = False
            else:
                resp = True
                logging.warning('you enter wrong number, repeat please')
        return choice

    def choose_pet(self):
        tamagochs = [pets.Dog(), pets.Robot(), pets.Python(), pets.MickyMouse(), pets.Cheburashka()]
        x = True
        while x:
            x = input('There are our pets \n1 - {0[0]} \n2 - {0[1]} \n3 - {0[2]} \n4 - {0[3]} \n5 - {0[4]} \nPlease choose your pet: '.format(tamagochs))
            try:
                pet = tamagochs[int(x)-1]
                x = False
            except:
                logging.warning('you enter wrong number, repeat please')
        return pet

    def ask_question(self, question):
        """
        use for asking question
        :param question: gameplay question
        :return: user response to question
        """
        response = input(question)
        return response

    def menu(self):
        """
         give to user menu's ways
         :return: number of way
         """
        print("""
         Choose way:
         #1 - New game
         #2 - Load gane
         #3 - Quit
               """)
        condition = ('1', '2', '3')
        resp = True
        while resp:
            choice = self.ask_question('Enter number of way: ')
            if choice in condition:
                resp = False
            else:
                resp = True
                logging.warning('you enter wrong number, repeat please')
        return choice

