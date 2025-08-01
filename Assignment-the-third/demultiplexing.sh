#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --cpus-per-task=16                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH --nodes=1
#SBATCH --output=output_%j.log   # STDOUT
#SBATCH --error=error_%j.log     # STDERR
#SBATCH --mail-user=ewi@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email 
set -e 

filepath="/projects/bgmp/shared/2017_sequencing/"
output="/projects/bgmp/ewi/bioinfo/Bi621/PS/Demultiplex-/output_demultiplex_NO_CUTOFF"
/usr/bin/time -v ./demultiplexing.py -O $output -I $filepath --qual_score_cutoff_indexes 0 