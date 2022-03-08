import sys
import math
""" profile:
    https://www.codingame.com/profile/26a6c9ea9318d0aae4416bb2c86d513c6337854
"""
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mines = []
exts = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mines.append( (ext.lower(), mt) )
    exts.append(ext.lower())
for i in range(q):
    fname = input()  # One file name per line.
    try:
        name, ex = fname.rsplit('.', 1)
        ex = ex.lower()
    except:
        print('UNKNOWN')
        continue
    try:
        if ex not in exts:
            print('UNKNOWN')
        else:
            for i in range( len(mines) ):
                if ex and mines[i][0] == ex:
                    print(mines[i][1])
                    break
    except:
        print('UNKNOWN')
        continue
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
# print("UNKNOWN")
