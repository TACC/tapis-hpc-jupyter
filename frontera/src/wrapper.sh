#!/bin/bash
SESSION_FILE="$HOME/delete_me_to_end_session"

# create password
export PASSWORD=`date | md5sum | cut -c-32`

# run notebook in background
LOCAL_IPY_PORT=8888

export XDG_RUNTIME_DIR="$STOCKYARD/jupyter"

module load tacc-singularity/3.4.2
nohup singularity run '/work/05747/cicsvc/frontera/public/tapis-hpc-jupyter-assets/jupyter.simg' &

# use ssh for port forwarding
# echo Using ssh for port forwarding
START_PORT=50000
NODE_HOSTNAME_PREFIX=`hostname -s`
NODE_HOSTNAME_DOMAIN=`hostname -d`
NODE_HOSTNAME_LONG=`hostname -f`
# on Frontera IPY_HOSTNAME_PREFIX has the form c###-###
module load python3
LOGIN_IPY_PORT=`python3 get_port.py $START_PORT $NODE_HOSTNAME_PREFIX`

echo Port is $LOGIN_IPY_PORT

for i in `seq 5`; do
    ssh -f -g -N -R $LOGIN_IPY_PORT:$NODE_HOSTNAME_LONG:$LOCAL_IPY_PORT login$i
done

# send email notification
echo Your notebook is now running at http://$NODE_HOSTNAME_DOMAIN:$LOGIN_IPY_PORT with password $PASSWORD | mailx -s "Jupyter notebook now running" ${email}

# use file to kill job
echo $NODE_HOSTNAME_LONG $IPYTHON_PID > $SESSION_FILE
while [ -f $SESSION_FILE ] ; do
    sleep 10
done
