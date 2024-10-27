import streamlit as st
import numpy as np
import pandas as pd
import os
st.set_page_config(page_title="Borda Count Selection")
st.header("Borda Count Selection System")
st.write("""This app leverages a Borda Count system to award points to competitors in a ranked order""")
st.markdown("Here is a **[link](https://en.wikipedia.org/wiki/Borda_count)** to learn more about the Borda Count method.")
uploaded_data = st.file_uploader("Upload the file containing the rank", type=["csv", "xlsx"])

if uploaded_data is not None:
  if "xlsx" in str(uploaded_data.name):
    df = pd.read_excel(uploaded_data)
    # st.dataframe(df, use_container_width=True)
  elif "csv" in str(uploaded_data.name):
    df = pd.read_csv(uploaded_data)
    # st.dataframe(df, use_container_width=True)
  else:
    df = pd.DataFrame()
    st.error("Please upload a file in the csv or xlsx format")


  if len(df) > 0:
    st.write("Use the widget below to select the columns for voting. Select them in order of their preference")
    choices = st.multiselect(df.columns)
    new_df = df[choices]
    st.dataframe(new_df, use_container_width=True)
    
