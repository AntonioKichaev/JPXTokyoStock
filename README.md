JPXTokyoStock
==============================

testing cook

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------



## Как скачать датасет с кагла
- исполнить скрипт из папки [kaggle.py](src/settings/kaggle.py) он создаст файлик /users/youname/.kaggle/kaggle.json
- скачиваем файлы, запускаем из папки [make_original_dataset_from_kaggle](src/data/make_original_dataset_from_kaggle.py)
- после чего получим в папке `data/raw/` кучу файлов

## snakemake дальше
- из корневой папки делаем snakemake и получаем весь пайплайн.
- snakemake --cores=all


## workflow Snakemake
[config.yaml](workflow/config.yaml)
что есть сейчас через snakemake 
1. заполним config file своими переменными и запустим snakemake --cores=all 
2. на выходе получим скаченный датасет из кагла

## Что добавить для подхода
1. Линтеры
2. Тесты
3. flake blake
4. потом остальное