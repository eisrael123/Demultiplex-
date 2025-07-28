#!/usr/bin/env python
import matplotlib.pyplot as plt
import os
import sys



output = "/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/Assignment-the-first/data_for_p1.txt"
with open(output, 'r') as f:
    dist_r1 = eval(f.readline().strip())
    dist_r2 = eval(f.readline().strip())
    dist_idx1 = eval(f.readline().strip())
    dist_idx2 = eval(f.readline().strip())

    #R1
    means =[]
    for key,value in dist_r1.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(101), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for DNA Base Positions')
    plt.savefig("r1.png")
    plt.close()

    #R2
    means = []
    for key,value in dist_idx1.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(8), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for DNA Base Positions')
    plt.savefig("idx1.png")
    plt.close()

    #R3
    means = []
    for key,value in dist_idx2.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(8), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for DNA Base Positions')
    plt.savefig("idx2.png")
    plt.close()

    #R4
    means = []
    for key,value in dist_r2.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(101), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for DNA Base Positions')
    plt.savefig("r2.png")
    plt.close()
