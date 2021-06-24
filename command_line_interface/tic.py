
class Board():
    def __init__(self):
        self.one = " "
        self.two = " "
        self.three = " "
        self.four = " "
        self.five = " "
        self.six = " "
        self.seven = " "
        self.eight = " "
        self.nine = " "

    def show_board(self):
        print(f'''

                {self.one}            |    {self.two}       |    {self.three}
                             |            |
                _____________|____________|_______________
                {self.four}            |    {self.five}       |    {self.six}
                             |            |
                _____________|____________|_______________
               {self.seven}             |    {self.eight}       |    {self.nine}
                             |            |
                             |            |

    ''')

    def add_symbol(self, symbol, number):
        if number == 1:
            self.one = symbol
        elif number == 2:
            self.two = symbol
        elif number == 3:
            self.three = symbol
        elif number == 4:
            self.four = symbol
        elif number == 5:
            self.five = symbol
        elif number == 6:
            self.six = symbol
        elif number == 7:
            self.seven = symbol
        elif number == 8:
            self.eight = symbol
        elif number == 9:
            self.nine = symbol
