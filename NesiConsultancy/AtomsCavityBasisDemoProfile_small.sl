#!/bin/bash -e
#SBATCH --job-name=AtomsCavityBasisDemo # job name (shows up in the queue)
#SBATCH --time=0:10:00      # Walltime (HH:MM:SS)
#SBATCH --mem=512MB          # Memory in MB
#SBATCH --qos=debug          # debug QOS for high priority job tests

module purge
module load Python
python -m cProfile -o output.pstats AtomsCavityBasisDemo.py -c ./Configs/smallconfig.ini
gprof2dot --colour-nodes-by-selftime -f pstats output.pstats | \
    dot -Tpng -o output_small.png
