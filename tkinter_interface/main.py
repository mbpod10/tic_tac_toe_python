from tkinter import *
from PIL import Image
from user import User

# ___________________________________UI__________________________________________

YELLOW = "#f7f5dd"
SQUARES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

window = Tk()
o_image = PhotoImage(file='images/o.png')
o_image = o_image.subsample(10)
x_image = PhotoImage(file='images/x.png')
x_image = x_image.subsample(5)


window.title("Tic Tac Toe")
window.config(padx=20, pady=20, bg=YELLOW)
background_image = PhotoImage(file='images/bg.png')

player1 = User(symbol=x_image, user_number=1)
player2 = User(symbol=o_image, user_number=2)

player1.is_turn = True
current_player = player1
other_player = player2


def change_player(func_curr, func_other):
    global current_player, other_player
    new = func_other
    current_player = func_other
    other_player = new


# ___________________________________1__________________________________________
quad1 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad1.create_image(100, 100, image=background_image)
quad1.grid(column=1, row=0)


def callback1(event):
    global current_player, other_player
    if 1 in SQUARES:
        quad1.create_image(100, 100, image=current_player.symbol)
        quad1.itemconfig(background_image, image=current_player.symbol)
        new = other_player
        current_player = other_player
        other_player = new
        # change_player(func_curr=current_player, func_other=other_player)
        SQUARES.remove(1)
    else:
        print("This square has already been selected, please select again")


quad1.bind("<Button-1>", callback1)

# ___________________________________2__________________________________________
quad2 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")

quad2.create_image(100, 100, image=background_image)
quad2.grid(column=2, row=0)


def callback2(event):
    global current_player, other_player
    if 2 in SQUARES:
        quad2.create_image(100, 100, image=current_player.symbol)
        # quad2.itemconfig(current_player.symbol, image=o_image)
        quad2.itemconfig(background_image, image=current_player.symbol)
        # new = other_player
        # current_player = other_player
        # other_player = new
        change_player(func_curr=current_player, func_other=other_player)
        SQUARES.remove(2)
    else:
        print("This square has already been selected, please select again")


quad2.bind("<Button-1>", callback2)
# ___________________________________3__________________________________________


quad3 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad3.create_image(100, 100, image=background_image)
quad3.grid(column=3, row=0)


def callback3(event):
    global current_player, other_player
    if 3 in SQUARES:
        quad3.create_image(100, 100, image=current_player.symbol)
        # quad3.itemconfig(current_player.symbol, image=o_image)
        quad3.itemconfig(background_image, image=current_player.symbol)
        # new = other_player
        # current_player = other_player
        # other_player = new
        change_player(func_curr=current_player, func_other=other_player)
        SQUARES.remove(3)
    else:
        print("This square has already been selected, please select again")


quad3.bind("<Button-1>", callback3)
# ___________________________________4__________________________________________
quad4 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad4.create_image(100, 100, image=background_image)
quad4.grid(column=1, row=1)


def callback4(event):
    global current_player, other_player
    if 4 in SQUARES:
        quad4.create_image(100, 100, image=current_player.symbol)
        quad4.itemconfig(current_player.symbol, image=o_image)
        new = other_player
        current_player = other_player
        other_player = new
        SQUARES.remove(4)
    else:
        print("This square has already been selected, please select again")


quad4.bind("<Button-1>", callback4)
# ___________________________________5__________________________________________
quad5 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad5.create_image(100, 100, image=background_image)
quad5.grid(column=2, row=1)


def callback5(event):
    quad5.create_image(100, 100, image=current_player.symbol)
    quad5.itemconfig(current_player.symbol, image=o_image)


quad5.bind("<Button-1>", callback5)
# ___________________________________6__________________________________________
quad6 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad6.create_image(100, 100, image=background_image)
quad6.grid(column=3, row=1)


def callback6(event):
    quad6.create_image(100, 100, image=current_player.symbol)
    quad6.itemconfig(current_player.symbol, image=o_image)


quad6.bind("<Button-1>", callback6)
# ___________________________________7__________________________________________
quad7 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad7.create_image(100, 100, image=background_image)
quad7.grid(column=1, row=3)


def callback7(event):
    quad7.create_image(100, 100, image=current_player.symbol)
    quad7.itemconfig(current_player.symbol, image=o_image)


quad7.bind("<Button-1>", callback7)
# ___________________________________8__________________________________________
quad8 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad8.create_image(100, 100, image=background_image)
quad8.grid(column=2, row=3)


def callback8(event):
    quad8.create_image(100, 100, image=current_player.symbol)
    quad8.itemconfig(current_player.symbol, image=o_image)


quad8.bind("<Button-1>", callback8)
# ___________________________________9__________________________________________
quad9 = Canvas(width=200, height=200, highlightthickness=1,
               highlightbackground="black")
quad9.create_image(100, 100, image=background_image)
quad9.grid(column=3, row=3)


def callback9(event):
    quad9.create_image(100, 100, image=current_player.symbol)
    quad9.itemconfig(current_player.symbol, image=o_image)


quad9.bind("<Button-1>", callback9)

game_on = True
# while game_on:
#     quad1.bind("<Button-1>", callback1)
#     quad2.bind("<Button-1>", callback2)
#     quad3.bind("<Button-1>", callback3)

window.mainloop()