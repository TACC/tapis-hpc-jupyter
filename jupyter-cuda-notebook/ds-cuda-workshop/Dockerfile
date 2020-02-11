# image: taccsciapps/ds-cuda-workshop

from tensorflow/tensorflow:1.13.1-gpu-py3

RUN pip install sklearn
RUN pip install torch
RUN pip install keras
RUN pip install matplotlib
RUN pip install pandas
RUN pip install pillow
RUN pip install jupyter

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

RUN mkdir /opt/notebooks
RUN chmod 777 /opt/notebooks
# run jupyter config gen
RUN /usr/local/bin/jupyter notebook --generate-config
ENV XDG_RUNTIME_DIR=""
COPY run_sing.sh /bin/run_sing.sh
RUN chmod 755 /bin/run_sing.sh
CMD ["/bin/run_sing.sh"]
#RUN useradd -ms /bin/bash jupyter
RUN chown -R jupyter ~/.jupyter
#RUN cp /root/.jupyter/jupyter_notebook_config.py /home/jupyter/
#RUN cp ~/.jupyter/jupyter_notebook_config.py /home/jupyter/
RUN echo "\n\n# Set a password if PASSWORD is set\n\
import os\n\
if 'PASSWORD' in os.environ:\n\
\tfrom IPython.lib import passwd\n\
\tc.NotebookApp.password = passwd(os.environ['PASSWORD'])\n\
\tdel os.environ['PASSWORD']\n\n\
c.NotebookApp.iopub_data_rate_limit=10000000\n" >> /home/jupyter/.jupyter/jupyter_notebook_config.py 

USER jupyter
