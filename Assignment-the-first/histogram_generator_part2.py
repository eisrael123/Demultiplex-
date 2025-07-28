#!/usr/bin/env python

output = "/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/Assignment-the-first/data_for_p1.txt"
with open(output, 'r') as f:
    dict1 = eval(f.readline().strip())
    dict2 = eval(f.readline().strip())
    dict3 = eval(f.readline().strip())
    dict4 = eval(f.readline().strip())

    print(dict1)
    print(type(dict1))
