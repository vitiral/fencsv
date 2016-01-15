#!/usr/bin/python
from __future__ import print_function

import csv

import six

__version__ = '0.0.1'

pieces_str = "PNBRQK"
pieces_str += pieces_str.lower()
pieces = set(pieces_str)
valid_spaces = set(range(1,9))

def tofen(csvstr):
    '''Load a csv str and convert to fen string'''
    sio = six.StringIO(csvstr)
    sio.seek(0)
    reader = csv.reader(sio, delimiter='|', quoting=csv.QUOTE_MINIMAL)
    board = [r for r in reader]
    descstr = ' '.join(board[0])
    board = board[1:]
    boardstr = []
    rowstr = []
    for row in board:
        spaces = 0
        for c in row:
            if c == ' ':
                spaces += 1
            else:
                if spaces:
                    rowstr.append(str(spaces))
                    spaces = 0
                rowstr.append(c)
        if spaces:
            rowstr.append(str(spaces))
        boardstr.append(''.join(rowstr))
        rowstr = []

    return '/'.join(boardstr) + ' ' + descstr


def tocsv(fenstr):
    '''Load a fen str and convert to csv'''
    fen = fenstr.split()
    boardstr, desc = fen[0], fen[1:]
    # convert the board to rows of either a piece or a space
    board = [desc]  # description is the header
    cur_row = []
    for i, c in enumerate(boardstr):
        if c in pieces:
            cur_row.append(c)
        elif c == '/':  # new row
            board.append(cur_row)
            cur_row = []
        elif int(c) in valid_spaces:
            cur_row.extend(' ' * int(c))
        else:
            raise ValueError("invalid fenstr at index: {} char: {}"
                             .format(i, c))
    board.append(cur_row) 
    sio = six.StringIO()
    writer = csv.writer(sio, delimiter='|', quoting=csv.QUOTE_MINIMAL,
                        lineterminator='\n')
    writer.writerows(board)
    return sio.getvalue()


if __name__ == '__main__':
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    csvtxt = tocsv(fen)
    refen = tofen(csvtxt)
    print(tocsv(fen))
    print("compare:")
    print(fen)
    print(refen)
    assert refen == fen
