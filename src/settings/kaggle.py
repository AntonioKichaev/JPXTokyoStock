import json
import os
import getpass
# mac
KAGGLE_PATH = os.path.join('/Users', getpass.getuser(), '.kaggle', 'kaggle.json')
with open(KAGGLE_PATH, 'w+') as file:
    kaggle_user = 'youName' # https://www.kaggle.com/
    kaggle_key = 'youKey'
    json_data = {
        "username": kaggle_user,
        "key": kaggle_key
    }
    json.dump(json_data, file)
    os.chmod(KAGGLE_PATH,mode=777)
