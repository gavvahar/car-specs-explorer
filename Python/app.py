import streamlit as st
from data_utils import load_data

st.set_page_config(page_title="Car Specs & MPG Dashboard", layout="wide")

st.title("Car Specs & MPG Dashboard")

df = load_data()

st.dataframe(df)
