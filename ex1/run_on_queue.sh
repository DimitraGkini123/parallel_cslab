#!/bin/bash

## Give the Job a descriptive name
#PBS -N run_omp_gameoflife

## Output and error files
#PBS -o run_omp_gameoflife.out
#PBS -e run_omp_gameoflife.err

## How many machines should we get?
#PBS -l nodes=1:ppn=8

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start
## Run make in the src folder (modify properly)

module load openmp
cd /home/parallel/parlab02/ex1/openmp
export OMP_NUM_THREADS=4
./Game_Of_Life 1024 1000