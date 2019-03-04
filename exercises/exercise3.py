def main():
    game = [[1, 0, 1],
            [2, 1, 1],
            [2, 1, 1]]
    winner = check_state(game)
    pass


def check_rows(game):
    winner = 0
    for i in range(3):
        winner = check_row(game, i)
        if winner != 0:
            return winner
    pass


def check_row(game, i):
    if len(game[i]) == game[i].count(game[i][0]):
        return game[i][0]
    return 0


def check_col(game, i):
    if game[0][i] == game[1][i] == game[2][i]:
        return game[0][i]
    return 0
    pass


def check_cols(game):
    winner = 0
    for i in range(3):
        winner = check_col(game, i)
        if winner != 0:
            return winner
    pass


def check_main_diag(game):
    if game[0][0] == game[1][1] == game[2][2]:
        return game[1][1]
    return 0
    pass


def check_second_diag(game):
    winner = game[1][1]
    prev = winner
    for i in range(len(game[0])):
        for j in range(len(game[0])):
            if i + j == len(game[0]) - 1:
                if game[i][j] != winner:
                    return 0
    return winner

    pass


def check_diag(game):
    winner = 0
    if check_main_diag(game) != 0:
        winner = check_main_diag(game)
    elif check_second_diag(game) != 0:
        winner = check_second_diag(game)
    return winner
    pass


def check_state(game):
    if check_rows(game):
        print("The winner is {}!\nHe won with a row.".format(check_rows(game)))
        return check_rows(game)
    elif check_cols(game):
        print("The winner is {}!\nHe won with a column.".format(check_cols(game)))
        return check_cols(game)
    elif check_diag(game):
        print("The winner is {}!\nHe won with a diagonal.".format(check_diag(game)))
        return check_diag(game)
    pass
    print("The current game is tied.")
    return 0


if __name__ == '__main__':
    main()
