#!/bin/bash -e
#SBATCH --job-name=AtomsCavityBasisDemo # job name (shows up in the queue)
#SBATCH --time=08:00:00      # Walltime (HH:MM:SS)
#SBATCH --mem=50GB          # Memory in MB


#SBATCH --mail-type=ALL
#SBATCH --mail-user=mleo705@aucklanduni.ac.nz

module purge
module load Python
python -m cProfile -o output.pstats AtomsCavityBasisDemo.py -c ./Configs/largeconfig.ini
gprof2dot --colour-nodes-by-selftime -f pstats output.pstats | \
    dot -Tpng -o output_large.png
