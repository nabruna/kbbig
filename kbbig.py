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

print("Welcome, traveler! This KBBIG script will require you to answer a few questions first.")
print("\nPress Y to answer YES and N to answer NO, then hit ENTER to confirm.")

# Simple yes or no function that prompts user to type two possible answers.
# A third answer will loop the program back on itself.
def yesno(question):
    prompt = (f"{question}")
    reply = (input(prompt).lower().strip())
    while reply not in ['y', 'n']:
        print("\nOh my god, you had ONE job. Come on, read the previous lines more carefully and try again.")
        return yesno(question)
        # Honestly, I could keep this one going forever but I do not want to torture my user.
    if reply == "y":
        return True
    if reply == "n":
        return print("\nOh, okay then. I guess you're not the target demographic anyway."), sys.exit()

# Prompt questions!
print("\nDo you like playing tabletop RPG as a bard?")
reply = yesno(">")

print("\nTired of the same old bard instruments like fiddle or flute?")
reply = yesno(">")

print("\nIs your DM rolling his eyes as you tell him you'll be playing a bard? AGAIN?")
reply = yesno(">")

# Now for the generator... Simple input this time.
gen = input("""
Break the chain with this brand new Kate Bush Bard Instrument Generator! With over 30 options, the KBBIG is directly inspired by Kate Bush's discography and her love of experimental instruments.

Simply hit ENTER on your keyboard and it will generate an unconventional/rare instrument for your bard to specialize in!\n""")

# And that's it! Now for the reveal and loop:
chosen_instrument = random.choice(bard_instruments)

print(f"Your bard's brand new instrument is...... THE", chosen_instrument.upper() + "!")
print("\nDon't like your instrument? Hit R to generate another one or Q to quit this script.")

def another(question):
    prompt2 = (f"{question}")
    run2 = (input(prompt2).lower().strip())
    while run2 == 'r':
        print("\nYour bard's brand new instrument is...... THE", random.choice(bard_instruments).upper() + "!")
        print("\nDon't like your instrument? Hit R to generate another one or Q to quit this script.")
        return another(question)
    if run2 not in ['r', 'q']:
        print("\nLike I said, hit R for another instrument or Q to quit. Take it or leave it, sweetie.")
        return another(question)
    if run2 == 'q':
        return print("\nThank you for using KBBIG!"), sys.exit()

run2 = another(">")