from __future__ import print_function

import fencsv


STARTING = '''\
w|KQkq|-|0|1
r|n|b|q|k|b|n|r
p|p|p|p|p|p|p|p
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
P|P|P|P|P|P|P|P
R|N|B|Q|K|B|N|R
'''

MOVED_PAWN = '''\
b|KQkq|e3|0|1
r|n|b|q|k|b|n|r
p|p|p|p|p|p|p|p
 | | | | | | | 
 | | | | | | | 
 | | | |P| | | 
 | | | | | | | 
P|P|P|P| |P|P|P
R|N|B|Q|K|B|N|R
'''

KING_PAWN = '''\
w|-|-|5|39
 | | | |k| | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | |P| | | 
 | | | |K| | | 
'''



# some fen strings to convert back and forth
fenstrs = {
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1": STARTING,
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1": MOVED_PAWN,
    "4k3/8/8/8/8/8/4P3/4K3 w - - 5 39": KING_PAWN,
}

def do_convert(fenstr, times=2):
    '''convert the fenstr back and forth several times'''
    for _ in range(times):
        fenstr = fencsv.tofen(fencsv.tocsv(fenstr))
    return fenstr

def test_back_forth():
    '''Test that fen strings can be converted back and forth'''
    # i = 0
    for fenex in fenstrs:
        csv = fencsv.tocsv(fenex)
        fen = fencsv.tofen(csv)
        assert fen == fenex
        # i += 1; print("## TEST {i}\n{fen}\n{csv}\n".format(i=i, fen=fen, csv=csv))
        converted = do_convert(fenex, 2)
        assert converted == fenex
        converted = do_convert(fenex, 10)
        assert converted == fenex


def test_validated():
    '''Test that the human validated csv strings work'''
    for fenex, csvex in fenstrs.items():
        print("passed")
        fen = fencsv.tofen(csvex)
        assert fen == fenex
        csv = fencsv.tocsv(fenex)
        assert csv == csvex


if __name__ == '__main__':
    test_back_forth()
    test_validated()
