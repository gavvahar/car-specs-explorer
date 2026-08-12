# Car Specs & MPG Dashboard

A Streamlit dashboard for exploring car specs — horsepower, MPG, and price — built on Kaggle's "Car Features and MSRP" dataset (~11k vehicles, model years 1990-2017).

**Status: work in progress.** Data loading, cleaning, and sidebar filtering (Make / Year / Fuel Type) are working. Charts, KPIs, and the leaderboard are still being built — this README will get filled out further in a later polish pass.

## Setup

1. Clone the repo.
2. Create/activate the `car` conda environment: `conda env create -f environment.yml` (or `conda activate car` if it already exists).
3. Install dependencies: `pip install -r requirements.txt`.

## Dataset

The dataset isn't committed to the repo. Get it one of two ways:

- Kaggle CLI: `kaggle datasets download -d CooperUnion/cardataset -p data/ --unzip` (may require Kaggle API credentials at `~/.kaggle/kaggle.json` — generate one from your Kaggle account settings if the download prompts for auth)
- Manual: download from https://www.kaggle.com/datasets/CooperUnion/cardataset

Either way, place/rename the resulting CSV as `data/cars.csv`.

## Running

From the repo root:

```
streamlit run Python/app.py
```
