def main():
    game = [[1, 0, 1],
            [2, 0, 2],
            [0, 0, 0]]
    print("The current state of the game is {}".format(check_state(game)))
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

def check_cols(game):
    pass


def check_diag(game):
    pass


def check_state(game):
    if check_rows(game):
        return check_rows(game)
    elif check_cols(game):
        pass
    elif check_diag(game):
        pass
    return 0



if __name__ == '__main__':
    main()
