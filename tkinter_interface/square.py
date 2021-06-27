from tkinter import *


class Square(Canvas):
    def __init__(self, number, column, row, background_image):
        super().__init__(highlightthickness=2,
                         highlightbackground="black", width=200, height=200)
        self.number = number
        self.grid(column=column, row=row)
        self.create_image(100, 100, image=background_image)
        self.bind("<Button-1>", self.call_back)

    def call_back(self, event):
        print(self.number)
