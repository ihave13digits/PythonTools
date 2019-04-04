#!/usr/bin/python3

# TextStreaming by digits version 0.5 2018.12

from os import system
from sys import stdout, platform
from time import sleep

### Calling Text.clear() ### (clear screen)

''' Clears Terminal Screen

    Shorthand for os.system('clear'/'cls')

'''

### Calling Text.sstream() ### (simple stream)

''' Optional Keyword Arguments:

    spd: float
        Length of time between characters printed

    clr: 'b'
        Clear before text
'''

### Calling Text.cstream() ### (complex stream)

''' Optional Keyword Arguments:

    spd: float
        Length of time between characters printed

    dly: integer
        Length of time after text is finished printing

    hdr: string
        Header string to solid print before text stream

    hdr_m: integer
        Margin between header and stream

    end: string
        String to append at the end of text ((solid print, not iteration) main use is '\n', for a new line)

    end_x: integer
        Iteration of end (main use is setting gap between texts)

    clr: 'b', 'a', 'b+a'
        'b': Clear before text
        'a': Clear after text
        'b+a': Clear before and after text
'''

### Calling Text.fstream() ### (file stream)

''' Optional Keyword Arguments:

    spd: float
        Length of time between characters printed

    dly: integer
        Length of time after text is finished printing

    hdr: string
        Header string to solid print before text stream

    hdr_m: integer
        Margin between header and stream

    end: string
        String to append at the end of text ((solid print, not iteration) main use is '\n', for a new line)

    end_x: integer
        Iteration of end (main use is setting gap between texts)

    clr: 'b', 'a', 'b+a'
        'b': Clear before text
        'a': Clear after text
        'b+a': Clear before and after text
'''

### {SOURCE CODE} ###

clear_cmd = ''

if platform.startswith('win32'):
    clear_cmd = 'cls'
else:
    clear_cmd = 'clear'

class Text:

    def clear():
        system(clear_cmd)

    def sstream(txt, spd=0.06, clr=''):
        if clr == 'b':
            system(clear_cmd)
        for c in txt:
            stdout.write(c)
            stdout.flush()
            sleep(spd)
        print("")

    def cstream(txt, spd=0.06, dly=0, hdr='', hdr_m=1, end='', end_x=1, clr=''):
        if dly == 0:
            if clr == 'b':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)
            if hdr != '':
                print(hdr + '\n' * hdr_m)
            for c in txt:
                stdout.write(c)
                stdout.flush()
                sleep(spd)
            if clr == 'a':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)
            print(end * end_x, end='')

        if dly > 0:
            delay = spd * dly
            if clr == 'b':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)
            if hdr != '':
                print(hdr + '\n' * hdr_m)
            for c in txt:
                stdout.write(c)
                stdout.flush()
                sleep(spd)
            print(end * end_x, end='')
            sleep(delay)
            if clr == 'a':
                system(clear_cmd)
            if clr == 'b+a':
                system(clear_cmd)

    def fstream(text_file, spd=0.06, dly=0, hdr='', hdr_m=1, end='', end_x=1, clr=''):
        with open(text_file, 'r') as txt:
            if dly == 0:
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for char in txt:
                    for c in char:
                        stdout.write(c)
                        stdout.flush()
                        sleep(spd)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                print(end * end_x, end='')

            if dly > 0:
                delay = spd * dly
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for char in txt:
                    for c in char:
                        stdout.write(c)
                        stdout.flush()
                        sleep(spd)
                print(end * end_x, end='')
                sleep(delay)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
