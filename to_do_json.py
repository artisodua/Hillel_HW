import json
import sys
import os

class ToDoJson():
    def __init__(self, link=None):
        self._link = link

    def read_json_file(self):
        try:
            with open(self._link) as f:
                input_file = json.load(f)
        except FileNotFoundError:
            print('JSON FILES NOT FOUND!!!')
        else:
            return input_file

    def write_json_file(self, data=None):
        with open('new_json.json', 'w') as f:
            json.dump(data, f, indent=2)

    def puth_file(self):
        path_to_current_file = os.path.realpath(__file__)
        print('path to the current file:', path_to_current_file)

    def puth_folder(self):
        return sys.path