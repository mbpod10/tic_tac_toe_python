from tkinter import *
from tkinter import messagebox
from square import Square
from user import User

YELLOW = "#f7f5dd"
SQUARES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
FONT_NAME = "Ariel"


window = Tk()
window.title("Tic Tac Toe")
o_image = PhotoImage(file='images/o.png')
o_image = o_image.subsample(10)
x_image = PhotoImage(file='images/x.png')
x_image = x_image.subsample(5)
window.config(padx=20, pady=20, bg="lightblue", cursor="hand2")

background_image = PhotoImage(file='images/bg.png')

player1 = User(symbol=x_image, user_number=1, letter='X')
player2 = User(symbol=o_image, user_number=2, letter='O')


current_player = player1
other_player = player2


def restart_game():
    global SQUARES, current_player, other_player
    SQUARES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quad1 = Square(number=1, column=1, row=1,
                   background_image=background_image)
    quad1.bind("<Button-1>", lambda event: call_back(event, quad=quad1))

    quad2 = Square(number=2, column=2, row=1,
                   background_image=background_image)
    quad2.bind("<Button-1>", lambda event: call_back(event, quad=quad2))

    quad3 = Square(number=3, column=3, row=1,
                   background_image=background_image)
    quad3.bind("<Button-1>", lambda event: call_back(event, quad=quad3))

    quad4 = Square(number=4, column=1, row=2,
                   background_image=background_image)
    quad4.bind("<Button-1>", lambda event: call_back(event, quad=quad4))

    quad5 = Square(number=5, column=2, row=2,
                   background_image=background_image)
    quad5.bind("<Button-1>", lambda event: call_back(event, quad=quad5))

    quad6 = Square(number=6, column=3, row=2,
                   background_image=background_image)
    quad6.bind("<Button-1>", lambda event: call_back(event, quad=quad6))

    quad7 = Square(number=7, column=1, row=3,
                   background_image=background_image)
    quad7.bind("<Button-1>", lambda event: call_back(event, quad=quad7))

    quad8 = Square(number=8, column=2, row=3,
                   background_image=background_image)
    quad8.bind("<Button-1>", lambda event: call_back(event, quad=quad8))

    quad9 = Square(number=9, column=3, row=3,
                   background_image=background_image)
    quad9.bind("<Button-1>", lambda event: call_back(event, quad=quad9))
    current_player.winner = False
    current_player.squares = []
    other_player.squares = []


def change_player():
    global current_player, other_player
    print(f"{current_player.user_number} {current_player.squares}")
    if current_player.winner:
        turn_canvas.itemconfig(
            language_text, text=f"{current_player.user_number} Wins!", fill='black')
        messagebox.showinfo(title='Winner!',
                            message=f"{current_player.user_number} Wins!")
        restart_game()
    elif len(SQUARES) == 0:
        turn_canvas.itemconfig(
            language_text, text=f"DRAW!", fill='black')
        messagebox.showinfo(title='Draw!',
                            message=f"No One Wins!")
        restart_game()
    else:
        new = current_player
        current_player = other_player
        other_player = new
        turn_canvas.itemconfig(
            language_text, text=f"{current_player.user_number} ({current_player.letter}) Turn", fill='black')


def call_back(event, **kwargs):
    print(kwargs['quad'].number)
    if kwargs['quad'].number in SQUARES:
        kwargs['quad'].create_image(100, 100, image=current_player.symbol)
        kwargs['quad'].itemconfig(
            background_image, image=current_player.symbol)
        current_player.pick_square(square=kwargs['quad'].number)
        SQUARES.remove(kwargs['quad'].number)
        change_player()

    else:
        print("This square has already been selected, please select again")


quad1 = Square(number=1, column=1, row=1, background_image=background_image)
quad1.bind("<Button-1>", lambda event: call_back(event, quad=quad1))

quad2 = Square(number=2, column=2, row=1, background_image=background_image)
quad2.bind("<Button-1>", lambda event: call_back(event, quad=quad2))

quad3 = Square(number=3, column=3, row=1, background_image=background_image)
quad3.bind("<Button-1>", lambda event: call_back(event, quad=quad3))

quad4 = Square(number=4, column=1, row=2, background_image=background_image)
quad4.bind("<Button-1>", lambda event: call_back(event, quad=quad4))

quad5 = Square(number=5, column=2, row=2, background_image=background_image)
quad5.bind("<Button-1>", lambda event: call_back(event, quad=quad5))

quad6 = Square(number=6, column=3, row=2, background_image=background_image)
quad6.bind("<Button-1>", lambda event: call_back(event, quad=quad6))

quad7 = Square(number=7, column=1, row=3, background_image=background_image)
quad7.bind("<Button-1>", lambda event: call_back(event, quad=quad7))

quad8 = Square(number=8, column=2, row=3, background_image=background_image)
quad8.bind("<Button-1>", lambda event: call_back(event, quad=quad8))

quad9 = Square(number=9, column=3, row=3, background_image=background_image)
quad9.bind("<Button-1>", lambda event: call_back(event, quad=quad9))

turn_canvas = Canvas(width=600, height=100, highlightthickness=3,
                     highlightbackground="black")

turn_canvas.grid(column=1, row=4, columnspan=3)

language_text = turn_canvas.create_text(300, 50, text=f"{current_player.user_number} ({current_player.letter}) Turn", fill='black',
                                        font=(FONT_NAME, 40, 'italic'))


window.mainloop()
