"""
Wanted Poster
"""

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

from guizero import App, Text, Picture

def main():
    WIT = "#FFFFFF"
    BACKGRD_CLR = "#000B18"
    window = App("DM for reward!")
    window.bg = BACKGRD_CLR
    wanted_text = Text(window, "Wanted!")
    wanted_text.size = 50
    wanted_text.text_color = WIT
    wanted_text.font= "Calibri"
    cat = Picture(window, image="pictures/tabitha.png")
    cat.resize(500, 500)


    window.display()


if __name__ == '__main__':
    main()
