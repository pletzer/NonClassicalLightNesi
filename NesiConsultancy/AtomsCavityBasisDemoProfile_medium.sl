#!/bin/bash -e
#SBATCH --job-name=AtomsCavityBasisDemo # job name (shows up in the queue)
#SBATCH --time=0:20:00      # Walltime (HH:MM:SS)
#SBATCH --mem=10GB          # Memory in MB
#SBATCH --cpus-per-task=8

module purge
module load Python
module load forge
srun map --profile python AtomsCavityBasisDemo.py -c ./Configs/mediumconfig.ini
