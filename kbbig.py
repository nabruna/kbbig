import random
import sys

# Peek-a-boo! This list was selected directly from Kate Bush's albums' Wikipedia pages
# Conveniently, it's in alphabetical order!
bard_instruments = ['accordion', 'balalaika', 'beer bottles', 'bodhrán', 'boobam' ,
'bouzouki', 'clapper', 'didgeridoo', 'fujara', 'gamba', 'harmonica', 'harpsichord',
'kabosy', 'koto', 'lirone', 'mandocello', 'mandola', 'mandolin', 'musical bow',
'musical saw', 'pan flute', 'psaltery', 'sitar', 'standing bell', 'timpani', 'tin whistle',
'tupan', 'uilleann pipes', 'valiha', 'whistle']

# Simple yes or no function that prompts user to type two possible answers.
# A third answer will loop the program back on itself.
def yesno(question):
    prompt = (f"{question} Y/N? ")
    reply = (input(prompt).lower().strip())
    if reply not in ['y', 'n']:
        print("\nThis isn't a fanfiction, dummy! Press Y for YES or N for NO.")
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
input("""
Break the chain with this brand new Kate Bush Bard Instrument Generator! With over 30 options, the Kate Bush Bard Instrument Generator is directly inspired by Kate Bush's discography and her love of experimental instruments.

Simply press ENTER and it will generate an unconventional/rare instrument for your bard to specialize in!\n""")

chosen_instrument = random.choice(bard_instruments)

# And that's it! Now for the reveal:
print(f"Your bard's brand new instrument is...... THE", chosen_instrument.upper() + "!")
print("\nThank you for using KBBIG!")