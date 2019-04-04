#!/usr/bin/python3

# File i/o by digits version 1.2.2019.2

from os import path

# Example Data (set first_save to True on start)
TARG = {# Required Keys
        'first_save' : True,
        'file' : 'data.txt',
        # Optional Keys
        'name' : 'target',
        'complete' : 0.0
        }

class Data:

    def save(target):
        text_file = target['file']
        game_folder = path.dirname(__file__)
        save_folder = path.join(game_folder, 'save')
        with open(path.join(save_folder, text_file), 'w') as f:
            for attribute in target:
                if target['first_save'] == False:
                    if type(target[attribute]) == bool:
                        f.write(str(target[attribute]))
                        f.write("\n")
                    if type(target[attribute]) == str:
                        f.write(str(target[attribute]))
                        f.write("\n")
                    if type(target[attribute]) == int:
                        f.write(str(target[attribute]))
                        f.write("\n")
                    if type(target[attribute]) == float:
                        f.write(str(target[attribute]))
                        f.write("\n")
                elif target['first_save'] == True:
                    if type(target[attribute]) == bool:
                        f.write(str(target[attribute]))
                        f.write("\n")
                    if type(target[attribute]) == str:
                        f.write(str(target[attribute]))
                        f.write("\n")
                    if type(target[attribute]) == int:
                        f.write(str(target[attribute]))
                        f.write("\n")
                    if type(target[attribute]) == float:
                        f.write(str(target[attribute]))
                        f.write("\n")
                    target['first_save'] = False

    def load(target):
        try:
            text_file = target['file']
            game_folder = path.dirname(__file__)
            save_folder = path.join(game_folder, 'save')
            with open(path.join(save_folder, text_file), 'r') as f:
                for attribute in target:
                    if type(attribute) == bool:
                        target[attribute] = bool(f.readline().strip())
                    if type(attribute) == str:
                        target[attribute] = str(f.readline().strip())
                    if type(attribute) == int:
                        target[attribute] = int(f.readline().strip())
                    if type(attribute) == float:
                        target[attribute] = float(f.readline().strip())
                        #Data.finalize(target, attribute, float)
        except FileNotFoundError:
            print("No save data found")
            exit()
