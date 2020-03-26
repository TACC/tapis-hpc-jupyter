#!/bin/bash
SESSION_FILE="$HOME/delete_me_to_end_session"

# create password
export PASSWORD=`date | md5sum | cut -c-32`

# run notebook in background
LOCAL_IPY_PORT=8888

export XDG_RUNTIME_DIR="$STOCKYARD/jupyter"

NODE_HOSTNAME_PREFIX=`hostname -s`
NODE_HOSTNAME_DOMAIN=`hostname -d`
NODE_HOSTNAME_LONG=`hostname -f`
# on Frontera IPY_HOSTNAME_PREFIX has the form c###-###

for i in `seq 5`; do
    ssh -f -g -N -R $LOGIN_IPY_PORT:$NODE_HOSTNAME_LONG:$LOCAL_IPY_PORT login$i
done

module load tacc-singularity/3.4.2
module load python3
BATCH_QUEUE="${AGAVE_JOB_BATCH_QUEUE}"
if [ $BATCH_QUEUE == "rtx" ] || [ $BATCH_QUEUE == "rtx-dev" ]; then
    START_PORT=45000
    export LOGIN_IPY_PORT=`python3 get_port.py $START_PORT $NODE_HOSTNAME_PREFIX`
    nohup singularity run --nv '/work/projects/wma_apps/frontera/tapis-hpc-jupyter-assets/ds-cuda-workshop.simg' &
else
    START_PORT=50000
    export LOGIN_IPY_PORT=`python3 get_port.py $START_PORT $NODE_HOSTNAME_PREFIX`
    nohup singularity run '/work/projects/wma_apps/frontera/tapis-hpc-jupyter-assets/jupyter-v2.img' &
fi

echo Port is $LOGIN_IPY_PORT

# send email notification
echo -e "Your notebook is now running at https://frontera-portal.tacc.utexas.edu/apps/jupyter/$LOGIN_IPY_PORT with password $PASSWORD\n\n\nThis message was auto-generated. If you'd like to contact us, don't reply to this email. Instead, please submit a ticket at https://frontera-portal.tacc.utexas.edu/tickets/new." | mailx -v -s "Launch your Frontera HPC Jupyter notebook session" -S smtp=smtp://relay.tacc.utexas.edu -S from="Frontera Apps <no-reply@frontera.tacc.utexas.edu>" ${email}
# use file to kill job
echo $NODE_HOSTNAME_LONG $IPYTHON_PID > $SESSION_FILE
while [ -f $SESSION_FILE ] ; do
    sleep 10
done
