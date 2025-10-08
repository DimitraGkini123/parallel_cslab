#!/bin/bash

## Give the Job a descriptive name
#PBS -N run_fw

## Output and error files
#PBS -o run_fw.out
#PBS -e run_fw.err

## How many machines should we get?
#PBS -l nodes=1:ppn=8

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start
## Run make in the src folder (modify properly)

module load openmp
cd /home/parallel/parlab02/ex2/FW
export OMP_NUM_THREADS=64

#./fw 1024
./fw_sr 4096 64
#./fw_sr_1 2048 128
# ./fw_tiled 2048 128