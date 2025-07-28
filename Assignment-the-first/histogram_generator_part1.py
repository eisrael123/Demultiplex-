#!/usr/bin/env python 
import bioinfo  
import matplotlib.pyplot as plt
import os
import sys
import gzip 

dir = "/projects/bgmp/shared/2017_sequencing"
fileR1 = f"{dir}/1294_S1_L008_R1_001.fastq.gz"
fileR2 = f"{dir}/1294_S1_L008_R2_001.fastq.gz"
fileR3 = f"{dir}/1294_S1_L008_R3_001.fastq.gz"
fileR4 = f"{dir}/1294_S1_L008_R4_001.fastq.gz"


dist_r1 = {i:[0,0] for i in range(101)}
dist_r2 = {i:[0,0] for i in range(101)}
dist_idx1 = {i:[0,0] for i in range(8)}
dist_idx2 = {i:[0,0] for i in range(8)}
with (
    gzip.open(fileR1,"rt") as r1, 
    gzip.open(fileR2,"rt") as r2, 
    gzip.open(fileR3,"rt") as r3, 
    gzip.open(fileR4,"rt") as r4, 
):
    index = 1
    while True:     
        read1 = r1.readline().strip()
        index1 = r2.readline().strip()
        index2 = r3.readline().strip()
        read2 = r4.readline().strip()
        if read1 == '' or index1 == '' or index2 == '' or read2 == '':
            break
        if index%4 == 0:
            for j in range(101):
                if j < 8: #indexes only have 8 characters
                    qual_score_idx1 = bioinfo.convert_phred(index1[j])
                    qual_score_idx2 = bioinfo.convert_phred(index2[j])
                    sum, counts = dist_idx1.get(j,[0, 0])
                    dist_idx1[j] = [sum + qual_score_idx1, counts + 1]
                    sum, counts = dist_idx2.get(j,[0, 0])
                    dist_idx2[j] = [sum + qual_score_idx2, counts + 1]
                qual_score_r1 = bioinfo.convert_phred(read1[j])
                qual_score_r2 = bioinfo.convert_phred(read2[j])
                sum, counts = dist_r1.get(j,[0, 0])
                dist_r1[j] = [sum + qual_score_r1, counts + 1]
                sum, counts = dist_r2.get(j,[0, 0])
                dist_r2[j] = [sum + qual_score_r2, counts + 1]
            # print(dist_r1) 
            # print(dist_r2)
            # print(dist_idx1)
            # print(dist_idx2)
            # print(f"\n\n\n")
            # sys.exit()
            # break
        index += 1
    print(f"{dist_r1}")
    print(f"{dist_r2}")
    print(f"{dist_idx1}")
    print(f"{dist_idx2}")
    