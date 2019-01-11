import json
import time


class JSONstorage:
    """
    write data of games  in json file
    """

    def write_data(self, name, steps_amount, game_status):
        """write data to json file"""
        filePathNameWExt = '/home/dbulka/PycharmProjects/pyQAtest_tamagochi/saves/' + '[' + '.json'
        with open( filePathNameWExt, 'a') as f:
            data = {time.asctime(): {'name ': name, 'steps_amount ': steps_amount, 'game_status ' :game_status}}
            json_data = json.dump(data,f)

