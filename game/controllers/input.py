import keyboard

from pyQAtest_tamagochi.utils import JSONstorage
from pyQAtest_tamagochi.game.views import gaming



#initializate json_storage
storage = JSONstorage()

while True:
    if keyboard.is_pressed('^') and keyboard.is_pressed('S'):
        storage.write_data(gaming.pet.name, gaming.n, gaming.pet.alive)

