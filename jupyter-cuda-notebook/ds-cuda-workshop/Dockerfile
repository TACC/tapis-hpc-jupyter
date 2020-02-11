# image: taccsciapps/ds-cuda-workshop

from tensorflow/tensorflow:1.13.1-gpu-py3

RUN pip install sklearn torch keras matplotlib pandas jupyter

###################################################################
# Create jupyter user
###################################################################
# the default $NB_USER is jovyan, but we want the default user to be jupyter
# - create jupyter early
# - run all user installation commands as jupyter
# - add jupyter user to special uid
# Jupyter GIDs
ARG TACC_GID=65536
ARG AGAVE_GID=G-816877
# Parameterize GID
# 65536 is a dummy value since we now override user UID/GID at launch
#  using Docker nsmap. This should means it's only important for GIDs not
#  collide and that g+r(x) permissions are set where needed
ENV NB_USER=jupyter \
    NB_GID=${TACC_GID} \
    NB_GROUP=${TACC_GID} \
    SHELL=/bin/bash
RUN groupadd --gid 816877 ${AGAVE_GID} && \
    useradd --uid 458981 --gid ${AGAVE_GID} -m --home /home/jupyter --shell /bin/bash $NB_USER && \
    groupadd --gid ${NB_GID} ${NB_GROUP} && \
    usermod -a -G ${NB_GROUP} jupyter
# While not ideal, this is required since the users that are injected
# into the container do not exist.
ENV HOME=/home/jupyter \
    USER=jupyter \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
# Make primary group TACC_GID
RUN usermod -g ${NB_GROUP} jupyter


