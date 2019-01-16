import keyboard

from pyQAtest_tamagochi.utils import JSONstorage
from pyQAtest_tamagochi.game.controller import gaming

if __name__ == "__main__":

    #initializate json_storage
    storage = JSONstorage()
    #initializate process of saving game parametrs if users press '^S'
    while True:
        if keyboard.is_pressed('^') and keyboard.is_pressed('S'):
            storage.write_data(gaming.pet.name, gaming.n, gaming.pet.alive)

