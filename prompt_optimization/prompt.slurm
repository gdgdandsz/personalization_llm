#!/bin/bash

#SBATCH --job-name=prompt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=64GB
#SBATCH --time=3:00:00
#SBATCH --gres=gpu
#SBATCH --partition=a100_1,a100_2,v100,rtx8000
#SBATCH --output=prompt_0.1.out
#SBATCH --error=prompt_0.1.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wd2148@nyu.edu


# job info

# Singularity path
ext3_path=/scratch/wd2148/Singu/overlay-50G-10M.ext3
sif_path=/scratch/wd2148/Singu/cuda11.6.124-cudnn8.4.0.27-devel-ubuntu20.04.4.sif

singularity exec --nv \
--overlay ${ext3_path}:ro \
${sif_path} /bin/bash -c "
source /ext3/env.sh
cd prompt_optimization
python /scratch/wd2148/prompt_optimization/main.py"