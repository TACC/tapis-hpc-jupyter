singularity build workshop-cuda.simg docker://taccsciapps/ds-cuda-workshop

singularity run --nv workshop-cuda.simg

nvcc --version

nvidia-smi

python3:
  - import numpy
  - import tensorflow
  - import h5py
  - import keras
  - import torch
  - import pandas
  - import jupyter
  - import matplotlib
  - import numpy
  - import scipy
