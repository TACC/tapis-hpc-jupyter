# tapis-hpc-jupyter
Jupyter notebook Tapis apps for TACC HPCs

## Pre-requisites
- Link to getting a token using Tapis v2

## Deployment instructions
- Modify each definition below by replacing sections with [...] with relevant information
    - NOTE: When modifying `/home1/05747/[USERNAME]/work`, be sure to update the number after `/home1/` to the one matching your account
- POST each definition to Tapis

### Storage System
```curl -sk -H "Authorization: Bearer $ACCESS_TOKEN" -F "fileToUpload=@storage_system.json" https://api.tacc.utexas.edu/systems/v2```

### Execution System
```curl -sk -H "Authorization: Bearer $ACCESS_TOKEN" -F "fileToUpload=@execution_system.json" https://api.tacc.utexas.edu/systems/v2```

### App
```curl -sk -H "Authorization: Bearer $ACCESS_TOKEN" -F "fileToUpload=@app.json" https://api.tacc.utexas.edu/apps/v2```

### Job
```curl -X POST --data "@job.json" -H "Content-Type:application/json" -H "Authorization:Bearer $ACCESS_TOKEN" https://api.tacc.utexas.edu/jobs/v2?pretty=true```
