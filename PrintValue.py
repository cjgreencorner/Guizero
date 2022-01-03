"""
Print a given value in the REPL
"""

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

from guizero import App, TextBox, PushButton, Text, Picture


def text_box():
    global input_box
    print(input_box.value)


def knop():
    print("De knop werkt!")


def main():
    global input_box
    window = App("Casus opdracht!")
    BACKGRD_CLR = "#000000"

    window.bg = BACKGRD_CLR
    button = PushButton(window, knop, text="Knop!!")
    button.bg = "blue"
    button.text_size = 30
    text1 = Text(window, "Geef een waarde in!")
    text1.bg = "white"
    Text(window, "")
    input_box = TextBox(window)
    input_box.bg = "white"
    Text(window, "")
    button2 = PushButton(window, text_box, text="Send")
    button2.bg = "white"
    Picture(window, image="pictures/download.png")


    window.display()


if __name__ == '__main__':
    main()
