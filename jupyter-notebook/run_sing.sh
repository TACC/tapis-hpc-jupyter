# Change to jupyter directory if it exists
if [ -n "$STOCKYARD" ]; then
	echo "Changing to WORK directory"
	cd $STOCKYARD
        cp /home/jupyter/jupyter_notebook_config.py $STOCKYARD/jupyter_notebook_config.py
        echo "\n\nimport os\nc.NotebookApp.notebook_dir = '$HOME'" >> $STOCKYARD/jupyter_notebook_config.py
fi

exec /opt/conda/bin/jupyter notebook --notebook-dir=$HOME --ip=0.0.0.0 --port=8888
