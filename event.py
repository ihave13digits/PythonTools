#!/usr/bin/python3

from os import system
from sys import stdin

class Event:

    def get_key():
        system("stty raw -echo")
        c = stdin.read(1)
        system("stty -raw echo")
        return c
