#!/usr/bin/env python
import bioinfo

#output = "/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/TEST-input_FASTQ/testinputR1.fastq"
#output = "/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/TEST-input_FASTQ/testinputR2.fastq"
output = "/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/TEST-input_FASTQ/testinputR3.fastq"
#output = "/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/TEST-input_FASTQ/testinputR4.fastq"
with open(output, 'r') as f:
    index = 1
    counter = 1
    while True:   
        read = f.readline().strip()
        if read == '':
            break
        if index%4 == 0:
            print(f"{counter}: {bioinfo.qual_score(read)}")
            counter += 1
        index+=1
