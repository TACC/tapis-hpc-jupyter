# Change to jupyter directory if it exists
#if [ -n "$STOCKYARD" ]; then
#	echo "Changing to WORK directory"
#	cd $STOCKYARD
#        cp /home/jupyter/jupyter_notebook_config.py $STOCKYARD/jupyter_notebook_config.py
#        echo "\n\nimport os\nc.NotebookApp.notebook_dir = './home'" >> $STOCKYARD/jupyter_notebook_config.py
#fi
cd ~/
mkdir ./ds-cuda-workshop
mkdir ./ds-cuda-workshop/${JOB_OWNER}
cd ./ds-cuda-workshop/${JOB_OWNER}
mkdir .config
cp /home/jupyter/.jupyter/jupyter_notebook_config.py .config
export JUPYTER_CONFIG_DIR=$(pwd)/.config
printf "\n\nimport os\nc.NotebookApp.notebook_dir = \"$(pwd)/\"" >> .config/jupyter_notebook_config.py
exec /usr/local/bin/jupyter notebook  --ip=0.0.0.0 --port=8888
