from tkinter import *
from PIL import Image

YELLOW = "#f7f5dd"

window = Tk()
window.title("Tic Tac Toe")
window.config(padx=20, pady=20, bg=YELLOW)

quad1 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
background_image = PhotoImage(file='images/bg.png')
quad1.create_image(100, 100, image=background_image)
quad1.grid(column=1, row=0)

lock_image = PhotoImage(file='images/o.png')
lock_image = lock_image.subsample(10)


def callback1(event):
    quad1.create_image(100, 100, image=lock_image)
    quad1.itemconfig(background_image, image=lock_image)
    print("clicked at", event.x, event.y)


quad1.bind("<Button-1>", callback1)


quad2 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")

# quad2.create_image(100, 100, image=lock_image)
quad2.grid(column=2, row=0)


quad3 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad3.grid(column=3, row=0)

quad4 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad4.grid(column=1, row=1)

quad5 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad5.grid(column=2, row=1)

quad6 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad6.grid(column=3, row=1)

quad7 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad7.grid(column=1, row=3)

quad8 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad8.grid(column=2, row=3)

quad9 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad9.grid(column=3, row=3)


window.mainloop()
