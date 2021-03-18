import sys
import time
import networkx as nx


class GameException(Exception):
    msg = ''

    def __init__(self, msg):
        self.msg = msg


def main():
    # one-move mode:
    # python main.py input1.txt 7
    # interactive-mode
    # python main.py interactive input1.txt computer-next 7
    if 'interactive' in sys.argv:
        mode = sys.argv[1]
        f = sys.argv[2]
        n = sys.argv[3]
        depth = sys.argv[4]
    else:
        mode = 'one-move'
        n = 'NA'
        f = sys.argv[1]
        depth = sys.argv[2]
    rows = 6
    cols = 7
    board = []
    graph = nx.Graph
    human = 0
    computer = 0
    out = 'output.txt'

    with open(f, 'r') as file:
        for _ in range(rows):
            row = file.readline()
            board.append([int(char) for char in row.strip()])
        next_player = int(file.readline().strip())

    show_board(board)

    if mode == 'interactive':
        if n == 'computer-next':
            computer = next_player
            human = switch_player(computer)
        else:  # human-next
            human = next_player
            computer = switch_player(human)

        while not board_is_full(board):
            if next_player == human:
                valid_choice = False
                while not valid_choice:
                    chosen_col = int(input('Choose col: '))
                    try:
                        board = place_piece(board, chosen_col, next_player)
                        valid_choice = True
                    except GameException as e:
                        if e.msg == 'Chosen column is full':
                            print(e.msg)
            else:  # computers turn
                chosen_col = choose_move(board, computer, depth)
                time.sleep(1)
                print(f'Computer chooses column: {chosen_col}')
                board = place_piece(board, chosen_col, next_player)
            next_player = switch_player(next_player)
            show_board(board)
    else:  # one-move mode
        best_col = choose_move(board, next_player, depth)
        board = place_piece(board, best_col, next_player)
        next_player = switch_player(next_player)
        make_output(out, board, next_player)


def choose_move(board, next_player, depth):
    best_col = 0

    return best_col


def place_piece(board, col, player):
    top_row = -1

    for row in range(len(board)):
        if board[row][col] == 0:
            top_row = row
    if top_row == -1:
        raise GameException('Chosen column is full')

    board[top_row][col] = player
    return board


def board_is_full(board):
    for row in board:
        for place in row:
            if place == 0:
                return False
    return True


def show_board(board):
    for row in board:
        print(row)


def switch_player(p):
    return 1 if p == 2 else 2


def make_output(path, board, next_player):
    with open(path, 'w') as f:
        for row in board:
            for place in row:
                f.write(str(place))
            f.write('\n')
        f.write(str(next_player))
        f.write('\n')


if __name__ == "__main__":
    main()
