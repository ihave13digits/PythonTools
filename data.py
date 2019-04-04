#!/usr/bin/python3

# Data I/O by digits version 1.2.2019.3

from os import path, mkdir

# Example Targets

'''
NORMAL_TARG = {# Required Keys
        'file' : '.txt',
        'type' : '',
        'data' : {# Data Set
            },
        # Optional
        'item' : {# Raw Variables
            }
        }

NESTED_TARG = {# Required Keys
        'file' : '.txt',
        'type' : 'dict',
        'data' : {# Data Set
            'str' : {
                'type' : 'str',
                'data' : {
                    '' : ''
                    }},
            'bool' : {
                'type' : 'bool',
                'data' : {
                    '' : False
                    }},
            'int' : {
                'type' : 'int',
                'data' : {
                    '' : 0
                    }},
            'float' : {
                'type' : 'float',
                'data' : {
                    '' : 0.0
                    }},
            },
        # Optional
        'item' : {# Raw Variables
            }
        }
'''

root_folder = path.dirname(__file__)

try:
    mkdir(path.join(root_folder, 'save'))
    save_folder = path.join(root_folder, 'save')
except FileExistsError:
    save_folder = path.join(root_folder, 'save')

class Data:

    def save(target):
        text_file = target['file']
        with open(path.join(save_folder, text_file), 'w') as f:
            if target['type'] == 'dict':
                for d in target['data']:
                    for attribute in target['data'][d]['data']:
                        f.write(str(target['data'][d]['data'][attribute]))
                        f.write("\n")
            else:
                for attribute in target['data']:
                    f.write(str(target['data'][attribute]))
                    f.write("\n")

    def load(target):
        try:
            text_file = target['file']
            with open(path.join(save_folder, text_file), 'r') as f:
                if target['type'] == 'str':
                    for attribute in target['data']:
                        target['data'][attribute] = str(f.readline().strip())
                if target['type'] == 'bool':
                    for attribute in target['data']:
                        target['data'][attribute] = bool(f.readline().strip())
                if target['type'] == 'int':
                    for attribute in target['data']:
                        target['data'][attribute] = int(f.readline().strip())
                if target['type'] == 'float':
                    for attribute in target['data']:
                        target['data'][attribute] = float(f.readline().strip())
                if target['type'] == 'dict':
                    for d in target['data']:
                        for attribute in target['data'][d]['data']:
                            if target['data'][d]['type'] == 'str':
                                target['data'][d]['data'][attribute] = str(f.readline().strip())
                            if target['data'][d]['type'] == 'bool':
                                target['data'][d]['data'][attribute] = bool(f.readline().strip())
                            if target['data'][d]['type'] == 'int':
                                target['data'][d]['data'][attribute] = int(f.readline().strip())
                            if target['data'][d]['type'] == 'float':
                                target['data'][d]['data'][attribute] = float(f.readline().strip())
        except FileNotFoundError:
            print("No save data found")
