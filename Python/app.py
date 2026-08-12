import streamlit as st, plotly.express as px
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

st.subheader("Horsepower vs. Highway MPG")
fig_hp_mpg = px.scatter(
    filtered_df,
    x="engine_hp",
    y="highway_mpg",
    color="engine_fuel_type",
    labels={"engine_hp": "Engine HP", "highway_mpg": "Highway MPG", "engine_fuel_type": "Fuel Type"},
)
st.plotly_chart(fig_hp_mpg, use_container_width=True)

st.subheader("Avg Highway MPG by Vehicle Style")
style_mpg = filtered_df.groupby("vehicle_style")["highway_mpg"].mean().sort_values(ascending=False).reset_index()
fig_style_mpg = px.bar(
    style_mpg,
    x="vehicle_style",
    y="highway_mpg",
    labels={"vehicle_style": "Vehicle Style", "highway_mpg": "Avg Highway MPG"},
)
st.plotly_chart(fig_style_mpg, use_container_width=True)

st.subheader("Horsepower vs. MSRP")
fig_hp_msrp = px.scatter(
    filtered_df,
    x="engine_hp",
    y="msrp",
    color="engine_fuel_type",
    log_y=True,
    labels={"engine_hp": "Engine HP", "msrp": "MSRP", "engine_fuel_type": "Fuel Type"},
)
st.plotly_chart(fig_hp_msrp, use_container_width=True)

st.subheader("Trends by Model Year")
year_trend = filtered_df.groupby("year")[["engine_hp", "highway_mpg"]].mean().reset_index()
fig_hp_trend = px.line(
    year_trend,
    x="year",
    y="engine_hp",
    markers=True,
    labels={"year": "Year", "engine_hp": "Avg Engine HP"},
)
fig_mpg_trend = px.line(
    year_trend,
    x="year",
    y="highway_mpg",
    markers=True,
    labels={"year": "Year", "highway_mpg": "Avg Highway MPG"},
)
col4, col5 = st.columns(2)
col4.plotly_chart(fig_hp_trend, use_container_width=True)
col5.plotly_chart(fig_mpg_trend, use_container_width=True)

st.subheader("Top 10 Most Efficient Vehicles")
leaderboard_df = filtered_df[filtered_df["engine_hp"] > 0].copy()
leaderboard_df["efficiency_score"] = (leaderboard_df["highway_mpg"] / (leaderboard_df["engine_hp"] / 100)).round(2)
leaderboard_df = leaderboard_df.sort_values("efficiency_score", ascending=False).head(10)
st.dataframe(
    leaderboard_df[["make", "model", "year", "engine_hp", "highway_mpg", "efficiency_score"]],
    hide_index=True,
)

st.dataframe(filtered_df)
