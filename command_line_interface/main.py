from users import User
from tic import Board
from codex import codex

QUADRANTS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = User(symbol="x", user_number=1)
player2 = User(symbol="o", user_number=2)


board = Board()


game_on = True
player1.is_turn = True

board.show_board()


def check_board():
    global QUADRANTS
    global game_on
    if player1.winner or player2.winner:
        game_on = False
    if len(QUADRANTS) == 0:
        print("RESET GAME")
        board.one = " "
        board.two = " "
        board.three = " "
        board.four = " "
        board.five = " "
        board.six = " "
        board.seven = " "
        board.eight = " "
        board.nine = " "
        player2.squares = []
        player1.squares = []
        QUADRANTS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def player_pick(current_player, other_player):
    global game_on
    x = input(f"{current_player.user_number} to choose: ")
    if int(x) in QUADRANTS:
        current_player.pick_square(square=codex[x]['value'])
        board.add_symbol(symbol=current_player.symbol,
                         number=codex[x]['value'])
        board.show_board()
        QUADRANTS.remove(int(x))
        # if current_player.winner == True:
        #     game_on = False
        current_player.is_turn = False
        other_player.is_turn = True
    else:
        print(f"Sorry, {codex[x]['value']} has already been chosen!")
        board.show_board()
        player_pick(current_player=current_player, other_player=other_player)


while game_on:

    if player1.is_turn:
        check_board()
        player_pick(current_player=player1, other_player=player2)
    if player2.is_turn:
        check_board()
        player_pick(current_player=player2, other_player=player1)
