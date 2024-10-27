import streamlit as st
import numpy as np
import pandas as pd
import os
st.set_page_config(page_title="Borda Count Selection")
st.header("Borda Count Selection System")
st.write("""This app leverages a Borda Count system to award points to competitors in a ranked order""")
uploaded_data = st.file_uploader("Upload the file containing the rank", type=["csv", "xlsx"])
uploaded_data

if "xlsx" in uploaded_data:
  df = pd.read_excel(uploaded_data)
  st.dataframe(df)
elif "csv" in uploaded_data:
  df = pd.read_csv(uploaded_data)
  st.dataframe(df)
else:
  st.error("Please upload a file in the csv or xlsx format")
