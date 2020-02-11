# Change to jupyter directory if it exists
#if [ -n "$STOCKYARD" ]; then
#	echo "Changing to WORK directory"
#	cd $STOCKYARD
#        cp /home/jupyter/jupyter_notebook_config.py $STOCKYARD/jupyter_notebook_config.py
#        echo "\n\nimport os\nc.NotebookApp.notebook_dir = './home'" >> $STOCKYARD/jupyter_notebook_config.py
#fi
cd ~/
mkdir ./home
cd ./home
cp /home/jupyter/.jupyter/jupyter_notebook_config.py .
printf "\n\nimport os\nc.NotebookApp.notebook_dir = \"$(pwd)\"" >> jupyter_notebook_config.py
exec /usr/local/bin/jupyter notebook  --ip=0.0.0.0 --port=8888
