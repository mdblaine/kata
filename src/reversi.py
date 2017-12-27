#!/usr/bin/python


def rstrip(rstring):
    """
    Helper function to strip newlines and spaces from string
    :param rstring:
    :return: rstring without spaces or newlines
    """
    return rstring.replace(" ", "").replace("\n", "")


def rfluf(rstring):
    """
    Helper function to prettify (fluf) with newlines and spaces for pretty print
    :param rstring:
    :return: rstring with spaces and newlines
    """
    for i in range(9):
        rstring = rstring[:i+i*8] + '\n' + rstring[i+i*8:]
    return ' '.join(rstring)


def rinflate(rstring):
    """
    Helper function to inflate 1-D 8x8 reversi string to 1-D 10x10 reversi list with empty around
    the edges.
    :param rstring: 1-D 8x8 reversi representation
    :return: 1-D 10x10 reversi list representation
    """
    for i in range(9):
        rstring = rstring[:i*2+i*8] + '..' + rstring[i*2+i*8:]  # tack on first and last column
    return list('.........' + rstring + '.........')  # tack on first and last rows


def rdeflate(rlist):
    """
    Helper function to strip a 1-D 10x10 reversi list to a 1-D 8x8 reversi string
    :param rlist: 1-D 10x10 reversi list representation
    :return: 1-D 8x8 reversi string representation
    """
    rlist = rlist[10:90]  # strip first and last rows
    rstring = ''
    for i in range(9):
        rstring += ''.join(rlist[i*10+1:i*10+9])  # snag rows less first and last columns
    return rstring


def legal_moves(board):
    """
    see: http://codingdojo.org/kata/Reversi/
    Given a current board position together with information about whose turn it is, return a list of
    the legal moves for that player.
    The reversi board is modified to a 1-D 10x10 with a row of empty spaces around the edges. Then the
    current position is P=y*10+x where x and y are 0 to 9. This makes for simplicity so that the spaces
    surrounding P are [-11, -10, -9, -1, 1, 9, 10, 11]. Given the extra space around the edges we don't
    have to check at the 8x8 edges.
    :param board: string representing the reversi board. Only valid chars are: [.WB \n]
    :return: legal moves for that player
    """
    # TODO validate reversi board

    board = rstrip(board)
    turn = board[-1]
    if turn == 'W':
        opponent = 'B'
    else:
        opponent = 'W'

    board = rinflate(board[:-1])  # board is now a 10x10 1-D list / length of 100

    p_surrounding = (-11, -10, -9, -1, 1, 9, 10, 11)
    p_opposite = (11, 10, 9, 1, -1, -9, -10, -11)

    for i in range(11, 89):  # skip top and bottom rows // won't worry about first and last columns
        if board[i] == opponent:
            for j in range(8):  # check surrounding for possible moves
                if board[i+p_surrounding[j]] == '.' and board[i+p_opposite[j]] != '.':
                    k = 1  # p_opposite[j]*k goes in the opposite direction of p_surrounding[j]
                    # while board[i+p_opposite[j]*k] not in '.0' and 11 < i+p_opposite[j]*k < 89:
                    while board[i+p_opposite[j]*k] not in '.0':  # keep looking opposite of P until edge or legal move
                        if board[i+p_opposite[j]*k] == turn:
                            # found instance of turn opposite opponent piece P; mark as legal move
                            board[i+p_surrounding[j]] = '0'
                            break
                        k += 1
    return rfluf(rdeflate(board)) + ' ' + turn


def main():
    import sys
    if len(sys.argv) > 1:
        print(legal_moves(sys.argv[1].strip()))
    else:
        print('''Requires a valid board position with who's turn it is at the end.
(e.g. python reversi.py " ........ ........ ........ ...BW... ...WB... ........ ........ ........ B")''')


if __name__ == '__main__':
    main()
