import time
import random


def print_pause(message_to_print):
    time.sleep(2)
    print(message_to_print)


def intro():
    print_pause('You are in the scary, Northeastern town of Derry, Maine.')
    print_pause('A whisper escapes your lips: "I am in danger!"')
    print_pause('You are walking down Main Street and no one is around.')
    print_pause('Despite the empty street, you know you are being watched.')
    print_pause("""You notice a creepy storm drain,
    and a curious red balloon in a nearby tree.""")


def get_input(items):
    print_pause("""Would you like to grab the red balloon (1) from the tree,
    or approach the storm drain (2) ?""")
    response = input('Type 1 for "balloon" or 2 for "storm drain" here.\n')
    if response == "1":
        red_balloon(items)
    elif response == "2":
        approach_gutter(items)
    else:
        print_pause('You have not chosen wisely. Try again.')
        get_input(items)


def red_balloon(items):
    print_pause("""You have chosen to grab the red balloon from the tree.""")
    if "balloon" in items:
        print_pause("""... but you notice you have already grabbed
        the red balloon from the tree.""")
        get_input(items)
    else:
        items.append("balloon")
        print_pause("""You reach out and hold the balloon firmly. Now what?""")
        get_input(items)


def approach_gutter(items):
    print_pause("""Placing one foot in front of the other,
     you approach the storm drain.""")
    if "balloon" in items:
        face_pennywise()
    else:
        print_pause("""EEK! It's a CLOWN! What are you going to do?! """)
        print_pause("""You are not equipped with clown fighting magic. """)
        print_pause("""You may need something red... and ballooney.
        You stumble and run back. """)
        get_input(items)


def face_pennywise():
    print_pause('Your heart thumps.')
    print_pause('You see the clown.')
    print_pause('You hand him the red balloon.')
    print_pause("""You see his creepy,
    white-gloved hand reach from the storm drain and... """)
    print_pause('"Thank you, friend, for returning my balloon."')
    print_pause("I will let you live if you roll a six on my die.")
    print_pause('Pennywise smiles diabolically. He shakes the die at you.')
    print_pause('You take the die in your hand and roll.')
    life_or_death = random.randint(1, 6)
    if life_or_death == 6:
        print_pause("""Pennywise does NOT embody your worst fear.
        You rolled a 6!""")
        print_pause("Instead, he shrivels and dies.  YOU WON!!!!!")
        play_again()
    else:
        random_quote()
        print_pause(f"You rolled a {life_or_death}.")
        print_pause("Pennywise embodies your greatest fear.")
        print_pause("You lost. Pennywise doesn't care.")
        play_again()


def play_again():
    response = input('PLAY AGAIN? Write Y for yes or N for no.\n').lower()
    if response == "y":
        play_pennywise()
    elif response == "n":
        print_pause("Wave goodbye to Pennywise!")
    else:
        print_pause("I have NO idea what you mean.")
        play_again()


def random_quote():
    losers = """Losers don't write the history books!"""
    fools = """Only a fool wants war!"""
    watch = """Watch this!"""
    step = """Step on a lego!"""
    love = """Love stinks!"""
    random_quote_list = [losers, fools, watch, step, love]
    quote = random.choice(random_quote_list)
    print_pause("Pennywise cries: ")
    print_pause(quote)


def play_pennywise():
    items = []
    intro()
    get_input(items)


play_pennywise()
