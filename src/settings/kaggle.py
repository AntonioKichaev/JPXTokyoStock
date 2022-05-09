import json
import os
import getpass

# mac
import click


@click.command
@click.argument('user', type=click.STRING)
@click.argument('key', type=click.STRING)
@click.argument('json_path', type=click.STRING)
def save_kaggle_creds(user: str, key: str, json_path: str):

    KAGGLE_PATH = json_path  # os.path.join('/Users', getpass.getuser(), '.kaggle', 'kaggle.json')
    with open(KAGGLE_PATH, 'w+') as file:
        json_data = {
            "username": user,
            "key": key
        }
        json.dump(json_data, file)
        os.chmod(KAGGLE_PATH, mode=777)


if __name__ == "__main__":
    save_kaggle_creds()
