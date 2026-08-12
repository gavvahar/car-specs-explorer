import pandas as pd, streamlit as st

COLUMN_RENAME_MAP = {
    "Make": "make",
    "Model": "model",
    "Year": "year",
    "Engine Fuel Type": "engine_fuel_type",
    "Engine HP": "engine_hp",
    "Engine Cylinders": "engine_cylinders",
    "Transmission Type": "transmission_type",
    "Driven_Wheels": "driven_wheels",
    "Number of Doors": "number_of_doors",
    "Market Category": "market_category",
    "Vehicle Size": "vehicle_size",
    "Vehicle Style": "vehicle_style",
    "highway MPG": "highway_mpg",
    "city mpg": "city_mpg",
    "Popularity": "popularity",
    "MSRP": "msrp",
}

# Small null counts (69/30/6/3 rows out of 11914) in core spec/filter columns.
# Dropped rather than imputed: fabricating HP/cylinder/door/fuel-type values
# for real car models would misrepresent actual specs in a specs dashboard.
REQUIRED_COLUMNS = ["Engine HP", "Engine Cylinders", "Number of Doors", "Engine Fuel Type"]


@st.cache_data
def load_data(path="data/cars.csv"):
    df = pd.read_csv(path)
    df = df.dropna(subset=REQUIRED_COLUMNS)
    # Market Category is ~31% null; dropping would lose too much data, so
    # null becomes its own explicit category instead.
    df["Market Category"] = df["Market Category"].fillna("Not Specified")
    df = df.rename(columns=COLUMN_RENAME_MAP)
    return df.reset_index(drop=True)
