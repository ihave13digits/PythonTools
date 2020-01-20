#!/usr/bin/python3

import time

class Timer:

    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.time = 0
        self.timeout = 0

    def set_timer(self, t):
        self.timeout = t

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()

class Clock:

    def __init__(self):
        self.tf = 30
        self.fps = 0
        self.timer = Timer()
        self.wall_time = time.time()
        self.elapsed = self.elapsed()
        
        self.timer.set_fps(1/tf)

    def set_fps(self, fps):
        self.tf = fps

    def tick(self):
        self.timer.start()

    def get_fps(self):
        return self.fps

    def wall_time(self):
        self.wall_time = time.time()
        return self.wall_time

    def elapsed(self):
        self.elapsed = time.time() - self.start_time
        return self.time