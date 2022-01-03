"""
Spy Name Chooser
"""

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

from guizero import App, Text, PushButton
from random import choice


def choose_name():
    first_names = ["Barbara", "Woody", "Tiberius", "Smokey", "Jennifer", "Ruby"]
    last_names = ["Spindleshanks", "Mysterioso", "Dungeon", "Catseye", "Darkmeyer", "Flamingobreath"]
    spy_name = choice(first_names) + " " + choice(last_names)
    name.value = spy_name


def main():
    global name
    window = App("TOP SECRET!")

    Text(window, "Push the red button to find out your spy name!")
    button = PushButton(window, choose_name, text="Tell me!")
    button.bg = "red"
    button.text_size = 30
    name = Text(window, text="")

    window.display()


if __name__ == '__main__':
    main()
