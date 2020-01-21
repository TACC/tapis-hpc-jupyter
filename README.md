# tapis-hpc-jupyter
Jupyter notebook Tapis apps for TACC HPCs

NOTE:
> This implementation is designed to host the singularity images with the CIC service account to insure each job will not download a whole new set of images on a compute node. [Defined Here](/frontera/storage_system.json#L15)  There is also specific [code](/frontera/src/get_port.py) that computes a unique port to be opened on a login node.  If on a system with a different configuration, it may be neccessary to alter this script.   

## Pre-requisites
- Have an Oauth client setup and generate a token. [Link to Documentation](https://tacc-cloud.readthedocs.io/projects/agave/en/latest/agave/introduction/tutorials.html#create-an-oauth-client)

## Deployment instructions
- Modify each definition below by replacing sections with [...] with relevant information
    - NOTE: When modifying `/home1/[05747]/[USERNAME]/work`, be sure to update the number after `/home1/` to the one matching your account
- POST each definition to Tapis
- Once deployed, an email will be sent to the email defined in the [job.json](/frontera/job.json)

### Storage System
```curl -sk -H "Authorization: Bearer $ACCESS_TOKEN" -F "fileToUpload=@storage_system.json" https://api.tacc.utexas.edu/systems/v2```

### Execution System
```curl -sk -H "Authorization: Bearer $ACCESS_TOKEN" -F "fileToUpload=@execution_system.json" https://api.tacc.utexas.edu/systems/v2```

### App
```curl -sk -H "Authorization: Bearer $ACCESS_TOKEN" -F "fileToUpload=@app.json" https://api.tacc.utexas.edu/apps/v2```

### Job
```curl -X POST --data "@job.json" -H "Content-Type:application/json" -H "Authorization:Bearer $ACCESS_TOKEN" https://api.tacc.utexas.edu/jobs/v2?pretty=true```
