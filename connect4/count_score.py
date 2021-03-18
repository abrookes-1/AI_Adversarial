def count_score(board):
    p1_score = 0
    p2_score = 0
    # Check` horizontally
    for row in board:
        # Check player 1
        if row[0:4] == [1] * 4:
            p1_score += 1

        if row[1:5] == [1] * 4:
            p1_score += 1

        if row[2:6] == [1] * 4:
            p1_score += 1

        if row[3:7] == [1] * 4:
            p1_score += 1
        # Check player 2

        if row[0:4] == [2] * 4:
            p2_score += 1

        if row[1:5] == [2] * 4:
            p2_score += 1

        if row[2:6] == [2] * 4:
            p2_score += 1

        if row[3:7] == [2] * 4:
            p2_score += 1

    # Check vertically
    for j in range(7):
        # Check player 1
        if (board[0][j] == 1 and board[1][j] == 1 and
                board[2][j] == 1 and board[3][j] == 1):
            p1_score += 1

        if (board[1][j] == 1 and board[2][j] == 1 and
                board[3][j] == 1 and board[4][j] == 1):
            p1_score += 1

        if (board[2][j] == 1 and board[3][j] == 1 and
                board[4][j] == 1 and board[5][j] == 1):
            p1_score += 1

        # Check player 2
        if (board[0][j] == 2 and board[1][j] == 2 and
                board[2][j] == 2 and board[3][j] == 2):
            p2_score += 1

        if (board[1][j] == 2 and board[2][j] == 2 and
                board[3][j] == 2 and board[4][j] == 2):
            p2_score += 1

        if (board[2][j] == 2 and board[3][j] == 2 and
                board[4][j] == 2 and board[5][j] == 2):
            p2_score += 1

    # Check diagonally
    # Check player 1        
    if (board[2][0] == 1 and board[3][1] == 1 and
            board[4][2] == 1 and board[5][3] == 1):
        p1_score += 1
    if (board[1][0] == 1 and board[2][1] == 1 and
            board[3][2] == 1 and board[4][3] == 1):
        p1_score += 1
    if (board[2][1] == 1 and board[3][2] == 1 and
            board[4][3] == 1 and board[5][4] == 1):
        p1_score += 1
    if (board[0][0] == 1 and board[1][1] == 1 and
            board[2][2] == 1 and board[3][3] == 1):
        p1_score += 1
    if (board[1][1] == 1 and board[2][2] == 1 and
            board[3][3] == 1 and board[4][4] == 1):
        p1_score += 1
    if (board[2][2] == 1 and board[3][3] == 1 and
            board[4][4] == 1 and board[5][5] == 1):
        p1_score += 1
    if (board[0][1] == 1 and board[1][2] == 1 and
            board[2][3] == 1 and board[3][4] == 1):
        p1_score += 1
    if (board[1][2] == 1 and board[2][3] == 1 and
            board[3][4] == 1 and board[4][5] == 1):
        p1_score += 1
    if (board[2][3] == 1 and board[3][4] == 1 and
            board[4][5] == 1 and board[5][6] == 1):
        p1_score += 1
    if (board[0][2] == 1 and board[1][3] == 1 and
            board[2][4] == 1 and board[3][5] == 1):
        p1_score += 1
    if (board[1][3] == 1 and board[2][4] == 1 and
            board[3][5] == 1 and board[4][6] == 1):
        p1_score += 1
    if (board[0][3] == 1 and board[1][4] == 1 and
            board[2][5] == 1 and board[3][6] == 1):
        p1_score += 1
    if (board[0][3] == 1 and board[1][2] == 1 and
            board[2][1] == 1 and board[3][0] == 1):
        p1_score += 1
    if (board[0][4] == 1 and board[1][3] == 1 and
            board[2][2] == 1 and board[3][1] == 1):
        p1_score += 1
    if (board[1][3] == 1 and board[2][2] == 1 and
            board[3][1] == 1 and board[4][0] == 1):
        p1_score += 1
    if (board[0][5] == 1 and board[1][4] == 1 and
            board[2][3] == 1 and board[3][2] == 1):
        p1_score += 1
    if (board[1][4] == 1 and board[2][3] == 1 and
            board[3][2] == 1 and board[4][1] == 1):
        p1_score += 1
    if (board[2][3] == 1 and board[3][2] == 1 and
            board[4][1] == 1 and board[5][0] == 1):
        p1_score += 1
    if (board[0][6] == 1 and board[1][5] == 1 and
            board[2][4] == 1 and board[3][3] == 1):
        p1_score += 1
    if (board[1][5] == 1 and board[2][4] == 1 and
            board[3][3] == 1 and board[4][2] == 1):
        p1_score += 1
    if (board[2][4] == 1 and board[3][3] == 1 and
            board[4][2] == 1 and board[5][1] == 1):
        p1_score += 1
    if (board[1][6] == 1 and board[2][5] == 1 and
            board[3][4] == 1 and board[4][3] == 1):
        p1_score += 1
    if (board[2][5] == 1 and board[3][4] == 1 and
            board[4][3] == 1 and board[5][2] == 1):
        p1_score += 1
    if (board[2][6] == 1 and board[3][5] == 1 and
            board[4][4] == 1 and board[5][3] == 1):
        p1_score += 1
    # Check player 2        
    if (board[2][0] == 2 and board[3][1] == 2 and
            board[4][2] == 2 and board[5][3] == 2):
        p2_score += 1
    if (board[1][0] == 2 and board[2][1] == 2 and
            board[3][2] == 2 and board[4][3] == 2):
        p2_score += 1
    if (board[2][1] == 2 and board[3][2] == 2 and
            board[4][3] == 2 and board[5][4] == 2):
        p2_score += 1
    if (board[0][0] == 2 and board[1][1] == 2 and
            board[2][2] == 2 and board[3][3] == 2):
        p2_score += 1
    if (board[1][1] == 2 and board[2][2] == 2 and
            board[3][3] == 2 and board[4][4] == 2):
        p2_score += 1
    if (board[2][2] == 2 and board[3][3] == 2 and
            board[4][4] == 2 and board[5][5] == 2):
        p2_score += 1
    if (board[0][1] == 2 and board[1][2] == 2 and
            board[2][3] == 2 and board[3][4] == 2):
        p2_score += 1
    if (board[1][2] == 2 and board[2][3] == 2 and
            board[3][4] == 2 and board[4][5] == 2):
        p2_score += 1
    if (board[2][3] == 2 and board[3][4] == 2 and
            board[4][5] == 2 and board[5][6] == 2):
        p2_score += 1
    if (board[0][2] == 2 and board[1][3] == 2 and
            board[2][4] == 2 and board[3][5] == 2):
        p2_score += 1
    if (board[1][3] == 2 and board[2][4] == 2 and
            board[3][5] == 2 and board[4][6] == 2):
        p2_score += 1
    if (board[0][3] == 2 and board[1][4] == 2 and
            board[2][5] == 2 and board[3][6] == 2):
        p2_score += 1
    if (board[0][3] == 2 and board[1][2] == 2 and
            board[2][1] == 2 and board[3][0] == 2):
        p2_score += 1
    if (board[0][4] == 2 and board[1][3] == 2 and
            board[2][2] == 2 and board[3][1] == 2):
        p2_score += 1
    if (board[1][3] == 2 and board[2][2] == 2 and
            board[3][1] == 2 and board[4][0] == 2):
        p2_score += 1
    if (board[0][5] == 2 and board[1][4] == 2 and
            board[2][3] == 2 and board[3][2] == 2):
        p2_score += 1
    if (board[1][4] == 2 and board[2][3] == 2 and
            board[3][2] == 2 and board[4][1] == 2):
        p2_score += 1
    if (board[2][3] == 2 and board[3][2] == 2 and
            board[4][1] == 2 and board[5][0] == 2):
        p2_score += 1
    if (board[0][6] == 2 and board[1][5] == 2 and
            board[2][4] == 2 and board[3][3] == 2):
        p2_score += 1
    if (board[1][5] == 2 and board[2][4] == 2 and
            board[3][3] == 2 and board[4][2] == 2):
        p2_score += 1
    if (board[2][4] == 2 and board[3][3] == 2 and
            board[4][2] == 2 and board[5][1] == 2):
        p2_score += 1
    if (board[1][6] == 2 and board[2][5] == 2 and
            board[3][4] == 2 and board[4][3] == 2):
        p2_score += 1
    if (board[2][5] == 2 and board[3][4] == 2 and
            board[4][3] == 2 and board[5][2] == 2):
        p2_score += 1
    if (board[2][6] == 2 and board[3][5] == 2 and
            board[4][4] == 2 and board[5][3] == 2):
        p2_score += 1

    return p1_score, p2_score
