import kaggle
import os
import logging
from pathlib import Path
import zipfile

logger = logging.getLogger(__name__)

PROJECT_PATH = Path(__file__).parent.parent.parent
DATA_PATH_RAW = os.path.join(PROJECT_PATH, 'data', 'raw')


def make_dataset_from_kaggle():
    kaggle.api.authenticate()
    competion = 'jpx-tokyo-stock-exchange-prediction'
    logger.warning(f'Start dowload files to {DATA_PATH_RAW} from competion {competion}')
    logger.warning(kaggle.api.competition_list_files(competion))

    kaggle.api.competition_download_files(competition=competion,
                                          path=DATA_PATH_RAW,
                                          force=False,
                                          quiet=False)
    logger.warning('Start unzip files')
    with zipfile.ZipFile(f'{os.path.join(DATA_PATH_RAW,competion)}.zip', 'r') as ziper:
        ziper.extractall(DATA_PATH_RAW)


if __name__ == "__main__":
    make_dataset_from_kaggle()
