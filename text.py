#!/usr/bin/python3

# TextStreaming by digits version 0.6 2018.12

import textwrap

from os import system
from sys import stdout, platform
from time import sleep

### Calling Text.clear() ### (clear screen)

'''

    Clears Terminal Screen

    Shorthand for os.system('clear'/'cls')
'''

### Calling Text.count_chars() ###

'''

    Counts total number of common characters in a given body of text

Keyword Arguments:

    txt: string
        body of text to be counted

'''

### Calling Text.show_chars() ###

'''

Optional Keyword Arguments:

    char: string
        Specific character to see the count of (note: if char is left empty, Text.show_chars() will return the entire dictionary of character values)

'''

### Calling Text.crypt() ###

'''

Keyword Argyments:

    txt: string
        String of text to encrypt or decrypt

Optional Keyword Arguments

    key: integer
        Encryption offset (note: 0 and any multiple of 94 will not work, fallback is 47 for a Ceasar Cypher effect)

    mode: string
        
        'e' - encrypt
        'd' - decrypt

'''

### Calling Text._stream ###

'''

Keyword Arguments for text streaming:

    txt: string
        String value

    r: integer
        Red value (1-255)

    g: integer
        Green value (1-255)

    b: integer
        Blue value (1-255)

Optional Keyword Arguments for text streaming:

    spd: float
        Length of time between characters printed

    dly: integer
        Length of time after text is finished printing

    hdr: string
        Header string to solid print before text stream

    hdr_m: integer
        Margin between header and stream

    end: string
        String to append at the end of text ((solid print, not iteration) main use is '', for appended text)

    end_x: integer
        Iteration of end (main use is setting gap between texts)

    wrp: integer
        Length of line for word wrap

    clr: 'b', 'a', 'b+a'
        'b': Clear before text
        'a': Clear after text
        'b+a': Clear before and after text
'''

### {SOURCE CODE} ###

text_characters = {#
        'A' : 0, 'a' : 0,
        'B' : 0, 'b' : 0,
        'C' : 0, 'c' : 0,
        'D' : 0, 'd' : 0,
        'E' : 0, 'e' : 0,
        'F' : 0, 'f' : 0,
        'G' : 0, 'g' : 0,
        'H' : 0, 'h' : 0,
        'I' : 0, 'i' : 0,
        'J' : 0, 'j' : 0,
        'K' : 0, 'k' : 0,
        'L' : 0, 'l' : 0,
        'M' : 0, 'm' : 0,
        'N' : 0, 'n' : 0,
        'O' : 0, 'o' : 0,
        'P' : 0, 'p' : 0,
        'Q' : 0, 'q' : 0,
        'R' : 0, 'r' : 0,
        'S' : 0, 's' : 0,
        'T' : 0, 't' : 0,
        'U' : 0, 'u' : 0,
        'V' : 0, 'v' : 0,
        'W' : 0, 'w' : 0,
        'X' : 0, 'x' : 0,
        'Y' : 0, 'y' : 0,
        'Z' : 0, 'z' : 0,
        '0' : 0,
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0,
        '6' : 0,
        '7' : 0,
        '8' : 0,
        '9' : 0,
        '`' : 0,
        '~' : 0,
        '!' : 0,
        '@' : 0,
        '#' : 0,
        '$' : 0,
        '%' : 0,
        '^' : 0,
        '&' : 0,
        '*' : 0,
        '(' : 0,
        ')' : 0,
        '-' : 0,
        '_' : 0,
        '=' : 0,
        '+' : 0,
        ',' : 0,
        '.' : 0,
        '<' : 0,
        '>' : 0,
        '/' : 0,
        '?' : 0,
        ';' : 0,
        ':' : 0,
        "'" : 0,
        '"' : 0,
        '[' : 0,
        ']' : 0,
        '{' : 0,
        '}' : 0,
        '|' : 0,
        ' ' : 0,
        '' : 0
        }

clear_cmd = ''

if platform.startswith('win32'):
    clear_cmd = 'cls'
else:
    clear_cmd = 'clear'

class Text:

    def clear():
        system(clear_cmd)

    def count_chars(txt):
        for char in txt:
            if char in text_characters:
                text_characters[char] += 1
            else:
                text_characters[''] += 1

    def show_chars(char=""):
        if char == "":
            return text_characters
        else:
            return text_characters[char]

    def clear_char_count():
        for char in text_characters:
            text_characters[char] = 0

    def crypt(txt, key=47, mode='e'):
        chars = "a0Z1b2Y3c4X5d6W7e8V9f`U~g,T.h?S!i@R#j$Q%k^P&l*O-m=N_n+M(o)L{p}K[q]J<r>I;s:H/t'G\"u|F vEwDxCyBzA"
        cypher = ""
        for c in txt:
            if c in chars:
                if mode == "e":
                    character = (chars.find(c) + key) % 94
                if mode == "d":
                    character = (chars.find(c) - key) % 94
                cypher += chars[character]
            else:
                cypher += c
        return cypher

    def sstream(txt, spd=0.06, wrp=1, clr=''):
        if wrp > 1:
            wrapped_txt = str('\n'.join(textwrap.wrap(txt, wrp, break_long_words=False)))
            if clr == 'b':
                system(clear_cmd)
            for c in wrapped_txt:
                stdout.write(c)
                stdout.flush()
                sleep(spd)
            print("")
        else:
            if clr == 'b':
                system(clear_cmd)
            for c in txt:
                stdout.write(c)
                stdout.flush()
                sleep(spd)
            print("")

    def cstream(txt, spd=0.06, dly=0, hdr='', hdr_m=1, end='\n', end_x=1, wrp=1, clr=''):
        if wrp > 1:
            wrapped_txt = str('\n'.join(textwrap.wrap(txt, wrp, break_long_words=False)))
            if dly == 0:
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for c in wrapped_txt:
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
                for c in wrapped_txt:
                    stdout.write(c)
                    stdout.flush()
                    sleep(spd)
                print(end * end_x, end='')
                sleep(delay)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
        else:
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

    def fstream(text_file, spd=0.06, dly=0, hdr='', hdr_m=1, end='\n', end_x=1, wrp=1, clr=''):
        with open(text_file, 'r') as txt:
            if wrp > 1:
                wrapped_txt = str('\n'.join(textwrap.wrap(txt.read(), wrp, break_long_words=False)))
                if dly == 0:
                    if clr == 'b':
                        system(clear_cmd)
                    if clr == 'b+a':
                        system(clear_cmd)
                    if hdr != '':
                        print(hdr + '\n' * hdr_m)
                    for char in wrapped_txt:
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
                    for char in wrapped_txt:
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
            else:
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

    def stream(text_file, r, g, b, spd=0.06, dly=0, hdr='', hdr_m=1, end='\n', end_x=1, wrp=1, clr=''):
        if '.txt' in text_file:
            FBG = 38#48
            with open(text_file, 'r') as txt:
                if wrp > 1:
                    wrapped_txt = str('\n'.join(textwrap.wrap(txt, wrp, break_long_words=False)))
                    if dly == 0:
                        if clr == 'b':
                            system(clear_cmd)
                        if clr == 'b+a':
                            system(clear_cmd)
                        if hdr != '':
                            print(hdr + '\n' * hdr_m)
                        for char in txt:
                            for c in char:
                                stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
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
                        for char in wrapped_txt:
                            for c in char:
                                stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                                stdout.flush()
                                sleep(spd)
                        print(end * end_x, end='')
                        sleep(delay)
                        if clr == 'a':
                            system(clear_cmd)
                        if clr == 'b+a':
                            system(clear_cmd)
        else:
            wrapped_txt = str('\n'.join(textwrap.wrap(text_file, wrp, break_long_words=False)))
            FBG=38#48
            if dly == 0:
                if clr == 'b':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for c in text_file:
                    stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
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
                for c in wrapped_txt:
                    stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                    stdout.flush()
                    sleep(spd)
                print(end * end_x, end='')
                sleep(delay)
                if clr == 'a':
                    system(clear_cmd)
                if clr == 'b+a':
                    system(clear_cmd)
