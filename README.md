# fencsv -- library to convert to/from fen strings and human readable csv

Fen strings are a way to indiciate state of a chessboard. You can read a
description about them here: https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation

Several python chess libraries use them, but none of them make them
easily human readable or human writable. That is the goal of this library.

# Spec

The file will have the following characteristics:
- The first row will contain the board description. This is fen
    fields 2 - 6. These will be separated by the '|' character
- The next 8 rows will contain the board state. Spaces indicate that no
    piece is present. Each piece will be separated by |

For instance, the following is the starting fenstr board position:
```
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

This is represented in fencsv as:

```
w|KQkq|-|0|1
r|n|b|q|k|b|n|r
p|p|p|p|p|p|p|p
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
P|P|P|P|P|P|P|P
R|N|B|Q|K|B|N|R
```

The first line is the fen state not related to piece position, except separated by
`|` instead of ` `. The other positions is the human readable board position.


Here is a completely blank board that you can use
```
w|KQkq|-|0|1
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
 | | | | | | | 
```
