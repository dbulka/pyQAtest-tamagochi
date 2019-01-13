import keyboard
from pyQAtest_tamagochi.game.views import GameInterface, User
from pyQAtest_tamagochi.game.models import pets
from pyQAtest_tamagochi.utils import JSONstorage


while True:
    if keyboard.is_pressed('s'):
        storage.write_data(pet.name, n, pet.alive)

