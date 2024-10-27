import streamlit as st
import numpy as np
import pandas as pd
import os
st.set_page_config(page_title="Borda Count Selection")
st.header("Borda Count Selection System")
st.write("""This app leverages a Borda Count system to award points to competitors in a ranked order""")
uploaded_data = st.file_uploader("Upload the file containing the rank", type=["csv", "xlsx"])

if uploaded_data is not None:
  if "xlsx" in str(uploaded_data.name):
    df = pd.read_excel(uploaded_data)
    st.dataframe(df, width=True)
  elif "csv" in str(uploaded_data.name):
    df = pd.read_csv(uploaded_data)
    st.dataframe(df, width=True)
  else:
    st.error("Please upload a file in the csv or xlsx format")
