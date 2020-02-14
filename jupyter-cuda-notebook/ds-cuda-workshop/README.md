# Testing Instructions

- Login to [DesignSafe](https://designsafe-ci.org)
- Go to the Research Workbench, click on Workspace, then click on the My Apps tab.
- Select Frontera HPC Jupyter
- Enter your email address
- Max job runtime (ex: `12:00:00`)
- Click the Run button and an email from DesignSafe Apps should arrive a second or two after the job starts running.
- In the email, click the link and use the password found in the email.
- Verify that a file named `delete_me_to_end_session` is in the directory listing 
- Terminal:
    - Click the `New` dropdown on the right and click Terminal
    - Verify the working directory to be `~/ds-cuda-workshop/[YOUR USERNAME]`
- Python:
    - Click the `New` dropdown on the right and click Python 3
    - In the notebook, attempt to import (and use if you want) these modules:
        ```import numpy
        import tensorflow
        import h5py
        import keras
        import torch
        import pandas
        import jupyter
        import matplotlib
        import numpy
        import scipy
        from PIL import Image
        ```
- Delete `delete_me_to_end_session`, wait 10 seconds, refresh the page and make sure the notebook is inaccessible.