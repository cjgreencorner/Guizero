"""
Meme maker
"""

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

from guizero import App, TextBox, Drawing, Combo, Slider


def draw_meme():
    meme.clear()
    meme.image(0, 0, "pictures/spongebob.png")
    meme.text(
        20, 20, top_text.value,
        color=color.value,
        size=size.value,
        font=font.value)
    meme.text(
        20, 320, bottom_text.value,
        color=color.value,
        size=size.value,
        font=font.value,
        )


# App

app = App("meme")

top_text = TextBox(app, "Me when the", command=draw_meme)
bottom_text = TextBox(app, "the", command=draw_meme)

color = Combo(app,
              options=["black", "white", "red", "green", "blue", "orange"],
              command=draw_meme, selected="blue")

font = Combo(app,
             options=["times new roman", "verdana", "courier", "impact"],
             command=draw_meme)

size = Slider(app, start=20, end=50, command=draw_meme)

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()