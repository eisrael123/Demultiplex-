#!/usr/bin/env python 
import bioinfo 
import gzip 
import argparse
import os 

def get_args():
    parser = argparse.ArgumentParser(description="Process input files and demultiplexes them into files seperated by index pairs.")
    parser.add_argument(
        '-I',
        '--input_dir',
        type=str,
        required=True,
        help='Path to the directory containing input files'
    )
    parser.add_argument(
        '-O',
        '--output_dir',
        type=str,
        default='/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/output_demultiplex',
        help='Path to the directory containing output files'
    )
    parser.add_argument(
        '--qual_score_cutoff_indexes',
        type=int,
        default=30,
        help='Quality score cutoff for indexes (default: 30)'
    )
    return parser.parse_args()

#parameters
args = get_args()
index_quality_cutoff = args.qual_score_cutoff_indexes
input_directory = args.input_dir
output_directory = args.output_dir

#initial variables
index_library = ['GTAGCGTA',
                 'AACAGCGA',
                 'CTCTGGAT',
                 'CACTTCAC',
                 'TATGGCAC',
                 'TCGACAAG',
                 'ATCGTGGT',
                 'GATCTTGC',
                 'CGATCGAT',
                 'TAGCCATG',
                 'TACCGGAT',
                 'GCTACTCT',
                 'TGTTCCGT',
                 'TCTTCGAC',
                 'TCGAGAGT',
                 'AGAGTCCA',
                 'GATCAAGG',
                 'CGGTAATC',
                 'CTAGCTCA',
                 'ACGATCAG',
                 'GTCCTAAG',
                 'ATCATGCG',
                 'TCGGATTC',
                 'AGGATAGC']
other_library = ['unknown',
                 'non-matching']
index_matches_counts = {}
index_hop_counts = {}
for index in index_library:
    for other_index in index_library:
        if index != other_index:
            key = f"{index}-{other_index}"
            index_hop_counts[key] = 0
index_unknown_counts = 0

#input 
input_files = []
for filename in os.listdir(input_directory):
    if filename.endswith('.gz') or filename.endswith('.fastq'):
        full_path = os.path.join(input_directory, filename)
        input_files.append(full_path)
order = ['R1', 'R2', 'R3', 'R4'] #order of input_files
def sort_key(filepath):
    basename = os.path.basename(filepath)
    for i, r in enumerate(order):
        if r in basename:
            return i
    return len(order)
input_files.sort(key=sort_key)

#output 
os.makedirs(output_directory, exist_ok=True)
open_files = {}
for index in index_library:
    index_matches_counts[index] = 0
    filename_r1 = f"{index}_R1.fastq"
    filename_r2 = f"{index}_R2.fastq"
    path_r1 = os.path.join(output_directory, filename_r1)
    path_r2 = os.path.join(output_directory, filename_r2)
    open_files[path_r1] = open(path_r1, 'w')
    open_files[path_r2] = open(path_r2, 'w')

for other in other_library:
    filename_r1 = f"{other}_R1.fastq"
    filename_r2 = f"{other}_R2.fastq"
    path_r1 = os.path.join(output_directory, filename_r1)
    path_r2 = os.path.join(output_directory, filename_r2)
    open_files[path_r1] = open(path_r1, 'w')
    open_files[path_r2] = open(path_r2, 'w')

# with(
#     open(input_files[0],'r') as r1,
#     open(input_files[1],'r') as r2,
#     open(input_files[2],'r') as r3,
#     open(input_files[3],'r') as r4
# ):
with(
    gzip.open(input_files[0],"rt") as r1, 
    gzip.open(input_files[1],"rt") as r2, 
    gzip.open(input_files[2],"rt") as r3, 
    gzip.open(input_files[3],"rt") as r4,
):
    while True:
        line_1_R1 = r1.readline().strip()
        line_2_R1 = r1.readline().strip()
        line_3_R1 = r1.readline().strip()
        line_4_R1 = r1.readline().strip()

        line_1_R2 = r2.readline().strip()
        line_2_R2 = r2.readline().strip()
        line_3_R2 = r2.readline().strip()
        line_4_R2 = r2.readline().strip()

        line_1_R3 = r3.readline().strip()
        line_2_R3 = r3.readline().strip()
        line_3_R3 = r3.readline().strip()
        line_4_R3 = r3.readline().strip()

        line_1_R4 = r4.readline().strip()
        line_2_R4 = r4.readline().strip()
        line_3_R4 = r4.readline().strip()
        line_4_R4 = r4.readline().strip()

        # Break if reached the end of each file
        if not (line_1_R1 and line_1_R2 and line_1_R3 and line_1_R4):
            break

        # Extract indexes from line 2 of R2 and R3
        index_R1 = line_2_R2
        index_R2 = line_2_R3

        headerR1 = f"{line_1_R1}{index_R1}-{index_R2}"
        headerR2 = f"{line_1_R4}{index_R1}-{index_R2}"

        index_R2 = bioinfo.reverse_complement(index_R2)
        #print(f"{line_1_R2}\n{index_R1}\n{line_3_R2}\n{line_4_R2}\n\n")
        #print(f"{index_R1}\t{index_R2}")
        # Case 1: record is undetermined
        if (bioinfo.qual_score(line_4_R2) < index_quality_cutoff or 
            bioinfo.qual_score(line_4_R3) < index_quality_cutoff or
            index_R1 not in index_library or
            index_R2 not in index_library):
            fileR1 = "unknown_R1.fastq"
            fileR2 = "unknown_R2.fastq"
            index_unknown_counts += 1
        # Case 2: record is index swapped
        elif index_R1 != index_R2:
            fileR1 = "non-matching_R1.fastq"
            fileR2 = "non-matching_R2.fastq"
            key = f"{index_R1}-{index_R2}"
            index_hop_counts[key] = index_hop_counts.get(key, 0) + 1
        # Case 3: record is a match
        else:
            fileR1 = f"{index_R1}_R1.fastq"
            fileR2 = f"{index_R2}_R2.fastq"
            index_matches_counts[index_R1] = index_matches_counts.get(index_R1, 0) + 1
        
        # Write records to the designated files
        outfile_R1 = os.path.join(output_directory, fileR1)
        open_files[outfile_R1].write(f"{headerR1}\n{line_2_R1}\n{line_3_R1}\n{line_4_R1}\n")
        outfile_R2 = os.path.join(output_directory, fileR2)
        open_files[outfile_R2].write(f"{headerR2}\n{line_2_R4}\n{line_3_R4}\n{line_4_R4}\n")

# Print index unknown counts
print(f"index unknown counts total = {index_unknown_counts}\n")

# Print index matches counts
print("index matches counts")
for index, value in index_matches_counts.items():
    print(f"\t{index} = {value}")
matches_total = sum(index_matches_counts.values())
print(f"total = {matches_total}")
print()

# Print index hop counts
print("index hop counts:")
for index_hop, value in index_hop_counts.items():
    print(f"\t{index_hop} = {value}")
hops_total = sum(index_hop_counts.values())
print(f"total = {hops_total}")
print()

# Print percentages
total = index_unknown_counts + matches_total + hops_total
index_matches_percent = (matches_total / total) * 100
index_hop_counts_percent = (hops_total / total) * 100
index_unknown_percent = (index_unknown_counts / total) * 100
print(f"% index matches: {index_matches_percent}")
print(f"% index hops: {index_hop_counts_percent}")
print(f"% index unknown: {index_unknown_percent}")



# Close all files
for f in open_files.values():
    f.close()

# Delete empty files
for filename in open_files.keys():
    if os.path.exists(filename) and os.path.getsize(filename) == 0:
        os.remove(filename)
