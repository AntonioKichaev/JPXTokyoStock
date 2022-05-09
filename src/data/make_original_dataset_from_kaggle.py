import kaggle
import os
import logging
from pathlib import Path
import zipfile
import click

logger = logging.getLogger(__name__)

PROJECT_PATH = Path(__file__).parent.parent.parent
DATA_PATH_RAW = os.path.join(PROJECT_PATH, 'data', 'raw')


@click.command
@click.argument('competion', type=click.STRING)
@click.argument('save_path_data', type=click.STRING)
def make_dataset_from_kaggle(competion: str, save_path_data: str):
    kaggle.api.authenticate()
    save_path_data = save_path_data or DATA_PATH_RAW
    logger.warning(f'Start dowload files to {save_path_data} from competion {competion}')

    logger.warning(kaggle.api.competition_list_files(competion))

    kaggle.api.competition_download_files(competition=competion,
                                          path=save_path_data,
                                          force=False,
                                          quiet=False)
    logger.warning('Start unzip files')
    with zipfile.ZipFile(f'{os.path.join(save_path_data, competion)}.zip', 'r') as ziper:
        ziper.extractall(save_path_data)


if __name__ == "__main__":
    make_dataset_from_kaggle()
