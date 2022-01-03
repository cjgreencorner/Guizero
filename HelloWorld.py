"""
Simple hello world test
"""

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

from guizero import App, Text


def main():
    window = App(title="Hello World")
    Text(window, text= "Hello World!")
    window.display()



if __name__ == '__main__':
    main()
