# tapis-hpc-jupyter
Jupyter notebook Tapis apps for TACC HPCs

## How to build and deploy the singularity image
- A docker image must be built first
    - ```docker build -t [REPO NAME]/jupyter-hpc-notebook:0.1 .```
- Push image to dockerhub
    - ```docker push [REPO NAME]/jupyter-hpc-notebook:0.1```
- Build singularity image
    - ```singularity build jupyter-hpc-notebook.img docker://[REPO NAME]/jupyter-hpc-notebook:0.1```
- Copy singularity image to personal account
    - ```scp jupyter-hpc-notebook.img [PERSONAL ACCOUNT]@frontera.tacc.utexas.edu:/work/[06281]/[PERSONAL ACCOUNT]/frontera/public/jupyter-hpc-notebook.img```
- Copy file from personal account to service account
    - ```ssh [SERVICE ACCOUNT]@frontera.tacc.utexas.edu```
    - ```scp [PERSONAL ACCOUNT]@frontera.tacc.utexas.edu:/work/[06281]/[PERSONAL ACCOUNT]/frontera/public/jupyter-hpc-notebook.img /work/[05747]/[SERVICE ACCOUNT]/frontera/public/tapis-hpc-jupyter-assets/jupyter.simg```
