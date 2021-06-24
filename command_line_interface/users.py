WINNING_SQUARES = [
    [1, 5, 9],
    [3, 5, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


class User():
    def __init__(self, symbol, user_number):
        self.squares = []
        self.symbol = symbol
        self.user_number = f"Player {user_number}"
        self.is_turn = False
        self.winner = False

    def show_user_info(self):
        if not self.squares:
            print(f"{self.user_number} has squares no squares")
        else:
            print(f"{self.user_number} has squares: {self.squares}")

    def pick_square(self, square):
        print(f"{self.user_number} picks {square}")
        self.squares.append(square)
        self.squares.sort()

        if len(self.squares) == 3:
            if self.squares in WINNING_SQUARES:
                print(f"{self.user_number} Wins!")
                self.winner = True

        if len(self.squares) > 3:
            split_array = self.squares
            for x in split_array:
                split_array.remove(x)
                split_array.sort()
                if split_array in WINNING_SQUARES:
                    print(f"{self.user_number} Wins!")
                    self.winner = True
                else:
                    split_array.append(x)
