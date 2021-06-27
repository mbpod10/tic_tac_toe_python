from tkinter import *
from square import Square

window = Tk()
window.title("Tic Tac Toe")
window.config(padx=20, pady=20, bg="lightblue", cursor="hand2")

background_image = PhotoImage(file='images/bg.png')

quad1 = Square(number=1, column=1, row=1, background_image=background_image)
quad2 = Square(number=2, column=2, row=1, background_image=background_image)
quad3 = Square(number=3, column=3, row=1, background_image=background_image)


window.mainloop()
