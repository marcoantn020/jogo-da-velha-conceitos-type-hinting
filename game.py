import random
from typing import List, Tuple


def display_board(board: List[str]) -> None:
    board[0] = '0'

    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print('-'*17)
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print('-'*17)
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print('\n\n\n\n\n\n\n')


def input_player() -> Tuple[str, str]:
    marker: str = ''
    print("Escolha [x] ou [o].Atenção a letra [o] representa a bolinha.")
    while not (marker == "X" or marker == "O"):
        marker = input("Jogador 1: Você quer ser [X] ou [O] >> ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board: List[str], marker: str, position: int) -> None:
    board[position] = marker


def win_checked(board: List[str], marker: str) -> bool:
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[1] == marker and board[2] == marker and board[3] == marker) or

            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or

            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker)
            )


def what_player_begin() -> str:
    if random.randint(0, 1) == 0:
        return "Jogador 1"
    else:
        return "jogador 2"


def check_space_empty(board: List[str], position: int) -> bool:
    return board[position] == " "


def check_full_board(board: List[str]) -> bool:
    for i in range(0, 10):
        if check_space_empty(board, i):
            return False
    return True


def next_player(board: List[str]) -> int:
    position: str = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space_empty(board, int(position)):
        print('\n')
        position = input("Faça sua jogada [1-9] >> ")[0]
        print('\n')

    return int(position)


def replay() -> bool:
    return input("Quer jogar de novo [S/N]? >> ")[0].upper().startswith('S')


# display_board([" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
print("="*41)
print("="*13, "Jogo da Velha", '='*13)
print("="*41)
while True:
    board: List[str] = [" "] * 10
    player_1: str
    player_2: str
    player_1, player_2 = input_player()

    turn: str = what_player_begin()

    playing: bool = True
    print("Jogador 1 escolheu [x/o] então.....")
    print("Jogador 2 começa.")
    while playing:
        if turn == "Jogador 1":
            display_board(board)
            position: int = next_player(board)
            place_marker(board, player_1, position)

        if win_checked(board, player_1):
            display_board(board)
            print("Você venceu!")
            playing = False
        else:
            if check_full_board(board):
                display_board(board)
                print("Empate")
                playing = False
            else:
                turn = "Jogador 2"
        # -------------------------------
        if turn == "Jogador 2":
            display_board(board)
            position: int = next_player(board)
            place_marker(board, player_2, position)

        if win_checked(board, player_2):
            display_board(board)
            print("Você venceu!")
            playing = False
        else:
            if check_full_board(board):
                display_board(board)
                print("Empate")
                playing = False
            else:
                turn = "Jogador 1"
    if not replay():
        break
