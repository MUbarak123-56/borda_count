import streamlit as st
import numpy as np
import pandas as pd
import os
st.set_page_config(page_title="Borda Count Selection", layout="wide")
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
    choices = st.multiselect("Make your selections", list(df.columns))
    n = len(choices)
    new_df = df[choices]
    st.dataframe(new_df, use_container_width=True)
    
    array_data = np.array(new_df)
    new_array = list(np.unique(array_data))
    df["id"] = df.index
    new_df = df.melt(id_vars="id", value_vars=df.columns, var_name="choice_rank", value_name="selection")
    final = new_df.pivot_table(index="id", columns=["selection"], values="choice_rank", aggfunc=lambda x: ' '.join(x))
    final = final.reset_index(drop=True)
    choice_order = choices
    order_dict = {}
    for i in range(n):
        order_dict[choice_order[i]] = n - i - 1
    final_df = final.replace(list(order_dict.keys()), list(order_dict.values()))
    rank_df = pd.DataFrame(final_df.sum(axis=0))
    rank_df = rank_df.rename(columns={0: "total_counts"})
    rank_df = rank_df.sort_values("total_counts", ascending=False).reset_index(drop=False)
    st.dataframe(rank_df)
    
    selected_list=list(rank_df.head(2)["selection"])
    st.markdown("**The winners are:**")
    for val in selected_list:
      st.markdown(val)
