import sys
from copy import deepcopy

from connect4.count_score import count_score


class GameException(Exception):
    msg = ''

    def __init__(self, msg):
        self.msg = msg


def main():
    # run one-move mode:
    # python main.py input1.txt 7
    # run interactive-mode
    # python main.py interactive input1.txt computer-next 7
    if 'interactive' in sys.argv:
        mode = sys.argv[1]
        f = sys.argv[2]
        n = sys.argv[3]
        depth = int(sys.argv[4])
    else:
        mode = 'one-move'
        n = 'NA'
        f = sys.argv[1]
        depth = int(sys.argv[2])
    rows = 6
    cols = 7
    board = []
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
                chosen_col = player_move(board, human)
            else:  # computers turn
                chosen_col, score = choose_move(board, computer, depth)
                # time.sleep(0.5)
                print(f'Computer chooses column: {chosen_col}')
            board = place_piece(board, chosen_col, next_player)

            next_player = switch_player(next_player)
            show_board(board)
    else:  # one-move mode
        if board_is_full(board):
            print('Game is complete')
        else:
            best_col, score = choose_move(board, next_player, depth)
            print(f'Computer chooses column {best_col} for player {next_player} with potential score {score}')
            board = place_piece(board, best_col, next_player)
            next_player = switch_player(next_player)
            show_board(board)
            make_output(out, board, next_player)


def choose_move(board, next_player, max_depth):
    best_score, best_col = minimax(board, max_depth, -1000000000, 1000000000, next_player)
    return best_col, best_score


def minimax(state, depth, alpha, beta, player):
    if depth == 0 or board_is_full(state):
        score = count_score(state)
        return score[0] - score[1], None

    # val = player1 score - player2 score
    # player1 is maximising
    best_eval = -1000000000 if player == 1 else 1000000000
    best_col = -1

    for i in get_valid_rows(state):
        child_state = place_piece(state, i, player)
        val, _ = minimax(child_state, depth-1, alpha, beta, switch_player(player))
        if player == 1:
            if val > best_eval:
                best_eval = val
                best_col = i
            if val > alpha:
                alpha = val
        else:
            if val < best_eval:
                best_eval = val
                best_col = i
            if val < alpha:
                alpha = val
        if beta <= alpha:
            break
    return best_eval, best_col


def player_move(board, player):
    valid_choice = False
    chosen_col = -1
    while not valid_choice:
        chosen_col = int(input('Choose col: '))
        try:
            place_piece(board, chosen_col, player)
            valid_choice = True
        except GameException as e:
            if e.msg == 'Chosen column is full':
                print(e.msg)
    return chosen_col


def place_piece(board, col, player):
    top_row = -1

    for row in range(len(board)):
        if board[row][col] == 0:
            top_row = row
    if top_row == -1:
        raise GameException('Chosen column is full')

    new_board = deepcopy(board)
    new_board[top_row][col] = player
    return new_board


def get_valid_rows(board):
    v = []
    for i in range(len(board[0])):
        if board[0][i] == 0:
            v.append(i)
    return v


def board_is_full(board):
    for place in board[0]:
        if place == 0:
            return False
    return True


def show_board(board):
    for row in board:
        for place in row:
            print(place, end=' ')
        print()


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
