#!/usr/bin/python3

# Classic Console Engine by digits version 1.0.2019.12

import random

from display import *
from event import *
from timer import *

class Engine:

    def __init__(self):
        self.running = True
        self.is_typing = False
        self.display = Display(32, 32)
        self.fps = 10
        self.sprites = []
        self.action_limit = 0
        self.action_queue = []
        
    def perform_action(self):
        K = Key()
        # Add Keypress to Action Queue
        self.event()
        actn = self.action_queue[0]

        ### Add Key Events Here ###
        if actn == "x":
            self.running = False
        
        # Clears Action Queue
        if len(self.action_queue) > self.action_limit:
            self.action_queue.pop(0)

    def event(self):
        # Get Key Press
        if self.is_typing == False:
            sel = Event.get_key(f=str)
        if self.is_typing == True:
            self.is_typing = False
            sel = input(": ")

        print(sel)
        self.action_queue.append(sel)

    def draw_sprites(self):
        if len(self.sprites) > 0:
            for s in self.sprites:
                self.display.draw_sprite(s)

    def start(self):
        self.run()

    def run(self):
        while self.running:
            self.display.new_display()
            self.draw_sprites()
            self.display.render()
            self.perform_action()

E = Engine()
E.start()
