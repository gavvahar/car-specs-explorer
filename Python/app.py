import streamlit as st
from data_utils import load_data

st.set_page_config(page_title="Car Specs & MPG Dashboard", layout="wide")

st.title("Car Specs & MPG Dashboard")

df = load_data()

st.sidebar.header("Filters")

makes = sorted(df["make"].unique())
selected_makes = st.sidebar.multiselect("Make", makes, default=makes)

min_year = int(df["year"].min())
max_year = int(df["year"].max())
year_range = st.sidebar.slider("Year", min_year, max_year, (min_year, max_year))

fuel_types = sorted(df["engine_fuel_type"].unique())
selected_fuel_types = st.sidebar.multiselect("Fuel Type", fuel_types, default=fuel_types)

mask = (
    df["make"].isin(selected_makes)
    & df["year"].between(year_range[0], year_range[1])
    & df["engine_fuel_type"].isin(selected_fuel_types)
)
filtered_df = df[mask]

count = len(filtered_df)
avg_mpg = f"{filtered_df['highway_mpg'].mean():.1f}" if count else "—"
avg_hp = f"{filtered_df['engine_hp'].mean():.1f}" if count else "—"

col1, col2, col3 = st.columns(3)
col1.metric("Avg Highway MPG", avg_mpg)
col2.metric("Avg Horsepower", avg_hp)
col3.metric("Models", count)

st.dataframe(filtered_df)
