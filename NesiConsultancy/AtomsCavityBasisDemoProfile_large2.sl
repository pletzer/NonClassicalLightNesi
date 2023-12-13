#!/bin/bash -e
#SBATCH --job-name=AtomsCavityBasisDemo # job name (shows up in the queue)
#SBATCH --time=02:00:00      # Walltime (HH:MM:SS)
#SBATCH --mem=50GB          # Memory in MB
#SBATCH --cpus-per-task=4   # number of threads

while getopts p: flag
do
    case "${flag}" in
       p) profiler=${OPTARG};;
    esac
done

module purge
module load Python

if [ "$profiler" == "map" ]; then
    echo "Using FORGE MAP..."
    module load forge
    srun map --profile python AtomsCavityBasisDemo.py -c ./Configs/largeconfig2.ini
else
    echo "Using GPROF..."
    python -m cProfile -o output.pstats AtomsCavityBasisDemo.py -c ./Configs/largeconfig2.ini
    gprof2dot --colour-nodes-by-selftime -f pstats output.pstats | \
    dot -Tpng -o output_large2.png
fi
