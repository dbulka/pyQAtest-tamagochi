import time
from multiprocessing import Process
from pyQAtest_tamagochi.game.controller import gaming
from pyQAtest_tamagochi.game.controller import input
from pyQAtest_tamagochi.game.controller import timer

process_gameplay = gaming
process_input = input
process_timer = timer

if __name__ == '__main__':
    Process(target=process_gameplay).start()
    Process(target=process_input).start()
    Process(target=process_timer).start()