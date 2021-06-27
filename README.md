## Tic Tac Toe (Tkinter)

Logic to see if a player has tic-tac-toe:
![winning_squares](https://i.imgur.com/rBp0I2E.jpg "SQUARES" =200x400)
<img src="https://i.imgur.com/rBp0I2E.jpg" alt="drawing" width="200" height=400/>

The squares are all labeled from 1 to 9. If a player has a winning combination of:
```python
WINNING_SQUARES = [
    [1, 5, 9],
    [3, 5, 7],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

that player would be the winner of the game.

Moreover, the logic to see if that winner has one of the combinations:
```python
def pick_square(self, square):
        print(f"{self.user_number} picks {square}")
        self.squares.append(square)
        self.squares.sort()

        if len(self.squares) >= 3:
            for arr in WINNING_SQUARES:
                return_arry = []
                for x in self.squares:
                    if x in arr:
                        return_arry.append(x)
                if return_arry == arr:
                    self.winner = True
```