# !/usr/bin/python3
# -*- coding: utf-8 -*-
# stream Babooshka

import random
import sys

# Peek-a-boo! This list was selected directly from Kate Bush's albums' Wikipedia pages
# Conveniently, it's in alphabetical order!
bard_instruments = ['accordion', 'balalaika', 'beer bottles', 'bells', 'bodhrán', 'boobam' ,
'bouzouki', 'bullroarer', 'Celtic harp', 'clapper', 'didgeridoo', 'fujara', 'gamba', 'harmonica', 'harmonium', 'harpsichord',
'kabosy', 'koto', 'lirone', 'mandocello', 'mandola', 'mandolin', 'musical bow',
'musical saw', 'pan flute', 'psaltery', 'renaissance guitar', 'sitar', 'standing bell', 'timpani', 'tin whistle',
'tupan', 'uilleann pipes', 'valiha', 'whistle']

# Instructions
print("""
Welcome to the Kate Bush Bard Instrument Generator (KBBIG)! With over 30 options, the KBBIG is directly inspired by Kate Bush's discography and her love of experimental instruments.

Simply hit ENTER on your keyboard and it will generate an unconventional/rare instrument for your bard to specialize in!""")

# The generator! This is written as a function because I want it to be. There's probably a better way to do this, but I'm lazy and this works.
def gen(int):
    prompt = (f"{int}")
    run = (input(prompt).lower().strip())
    while run not in ['q']:
        print("\nYour bard's brand new instrument is...... THE", random.choice(bard_instruments).upper() + "!")
        print("\nDon't like your instrument? Hit ENTER to generate another or quit this script by pressing Q.")
        return gen(int)
    if run == 'q':
        return print("\nThank you for using KBBIG!"), sys.exit()

run = gen(">")
