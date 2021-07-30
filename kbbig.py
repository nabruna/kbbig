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

# Now for the generator... Simple input.
gen = input("""
Welcome to the Kate Bush Bard Instrument Generator (KBBIG)! With over 30 options, the KBBIG is directly inspired by Kate Bush's discography and her love of experimental instruments.

Simply hit ENTER on your keyboard and it will generate an unconventional/rare instrument for your bard to specialize in!\n""")

# And that's it! There's probably a better way to do this that does not involve calling a
# new function again............. but I'm lazy and this works.
chosen_instrument = random.choice(bard_instruments)

print(f"Your bard's brand new instrument is...... THE", chosen_instrument.upper() + "!")
print("\nDon't like your instrument? Hit ENTER to generate another one or quit this script by pressing Q.")

def another(question):
    prompt2 = (f"{question}")
    run2 = (input(prompt2).lower().strip())
    while run2 not in ['q']:
        print("\nYour bard's brand new instrument is...... THE", random.choice(bard_instruments).upper() + "!")
        print("\nDon't like your instrument? Hit ENTER to generate another or quit this script by pressing Q.")
        return another(question)
    if run2 == 'q':
        return print("\nThank you for using KBBIG!"), sys.exit()

run2 = another(">")