#!/usr/bin/python3

import os, sys

class Key:

    def __init__(self):
        self.esc = ""

class Event:

    def get_key(f=str):
        os.system("stty raw -echo")
        c = sys.stdin.read(1)
        os.system("stty -raw echo")
        return f(c)

    def get_text():
        txt = input()
        return txt
