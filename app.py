import streamlit as st
import numpy as np
import pandas as pd
import os
st.set_page_config(page_title="Borda Count Selection")
st.header("Borda Count Selection System")
st.write("""This app leverages a Borda Count system to award points to competitors in a ranked order""")
data = st.file_uploader("Upload the file containing the rank", type=["csv", "xlsx"])
st.dataframe(data)
