# Image: tacc/csc_jupyter
from ubuntu:16.04
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

RUN apt-get install -y vim

# create notebook dir
RUN /opt/conda/bin/conda install jupyter -y  --quiet
RUN /opt/conda/bin/conda install -c conda-forge gridfill esmpy

RUN mkdir /opt/notebooks
RUN chmod 777 /opt/conda/bin/conda
RUN chmod 777 /opt/notebooks
RUN chmod 777 /opt/conda/bin/jupyter

# run jupyter config gen
RUN /opt/conda/bin/jupyter notebook --generate-config
# generate self-signed cert
# RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /root/mykey.key -out /root/mycert.pem -batch

# install additional packages
# RUN apt-get install -y vim crudini

# update jupyter config
# RUN crudini --set /root/.jupyter/jupyter_notebook_config.py '' c.NotebookApp.certfile \'/root/mycert.pem\'

# RUN crudini --set /root/.jupyter/jupyter_notebook_config.py '' c.NotebookApp.ip \'*\'

# RUN crudini --set /root/.jupyter/jupyter_notebook_config.py '' c.NotebookApp.keyfile \'/root/mykey.key\'

# RUN crudini --set /root/.jupyter/jupyter_notebook_config.py '' c.NotebookApp.notebook_dir \'/root/notebook\'

# RUN crudini --set /root/.jupyter/jupyter_notebook_config.py '' c.NotebookApp.open_browser False

# RUN crudini --set /root/.jupyter/jupyter_notebook_config.py '' c.NotebookApp.port 8887

ENV XDG_RUNTIME_DIR=""
#ENV HOME='$STOCKYARD/jupyter'
COPY run_sing.sh /bin/run_sing.sh
RUN chmod 755 /bin/run_sing.sh
#CMD ["tini", "--", "/bin/run_sing.sh"]
CMD ["/bin/run_sing.sh"]
RUN useradd -ms /bin/bash jupyter
RUN cp /root/.jupyter/jupyter_notebook_config.py /home/jupyter/
RUN echo "\n\n# Set a password if PASSWORD is set\n\
import os\n\
if 'PASSWORD' in os.environ:\n\
\tfrom IPython.lib import passwd\n\
\tc.NotebookApp.password = passwd(os.environ['PASSWORD'])\n\
\tdel os.environ['PASSWORD']\n\n\
c.NotebookApp.iopub_data_rate_limit=10000000\n" >> /home/jupyter/jupyter_notebook_config.py

USER jupyter

#CMD ["/opt/conda/bin/jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip=0.0.0.0", "--port=8888"]

