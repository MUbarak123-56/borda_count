import streamlit as st
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(rc={'axes.facecolor':(0,0,0,0), 'figure.facecolor':(0,0,0,0)})

# st.set_page_config(page_title="Borda Count Selection", layout="wide")
st.set_page_config(page_title="Borda Count Ranking")
st.header("Borda Count Ranking System")
st.write("""This app leverages a Borda Count system to award points to competitors in a ranked order""")
st.markdown("Here is a **[link](https://en.wikipedia.org/wiki/Borda_count)** to learn more about the Borda Count method.")

with st.expander("Open to see instructions on the data format that works well with this website"):
    st.write("""The format of the data that works well with the algorithm needs the choices listed as columns with each observations representing people's decisions""")
    st.write("""This is useful for selecting the right columns for running the algorithm.""")
    test_data = pd.read_excel("data_2.xlsx")
    st.write("Below is a sample of the data")
    st.dataframe(test_data.head(3), use_container_width=True)
  
uploaded_data = st.file_uploader("Upload the file containing the rank", type=["csv", "xlsx"])

if uploaded_data is not None:
  if "xlsx" in str(uploaded_data.name):
    df = pd.read_excel(uploaded_data)
    st.write("A preview of the uploaded data")
    st.dataframe(df.head(3), use_container_width=True)
  elif "csv" in str(uploaded_data.name):
    df = pd.read_csv(uploaded_data)
    st.write("A preview of the uploaded data")
    st.dataframe(df.head(3), use_container_width=True)
  else:
    df = pd.DataFrame()
    st.error("Please upload a file in the csv or xlsx format")


  if len(df) > 0:
  
    num_candidates = st.number_input("How many candidates would you like to select?", value = 0)
    st.write("Use the widget below to select the columns for voting. Select them in order of their rank")
    with st.form(key="Selecting columns"):
      choices = st.multiselect("Make your selections", list(df.columns), placeholder="Select the columns in order of rank")
      submit_button = st.form_submit_button(label="Submit")
      
    if submit_button:
      n = len(choices)
      new_df = df[choices]
      # st.dataframe(new_df, use_container_width=True)
      
      array_data = np.array(new_df)
      new_array = list(np.unique(array_data))
      new_df["id"] = new_df.index
      new_df = new_df.melt(id_vars="id", value_vars=new_df.columns, var_name="choice_rank", value_name="selection")
      final = new_df.pivot_table(index="id", columns=["selection"], values="choice_rank", aggfunc=lambda x: ' '.join(x))
      final = final.reset_index(drop=True)
      choice_order = choices
      order_dict = {}
      for i in range(n):
          order_dict[choice_order[i]] = n - i
      final_df = final.replace(list(order_dict.keys()), list(order_dict.values()))
      rank_df = pd.DataFrame(final_df.sum(axis=0))
      rank_df = rank_df.rename(columns={0: "total_counts"})
      rank_df = rank_df.sort_values("total_counts", ascending=False).reset_index(drop=False)
      rank_df["level"] = rank_df.index
      rank_df["grp"] = rank_df["level"].apply(lambda x: 1 if x < num_candidates else 0)
      #st.dataframe(rank_df)

      fig, ax = plt.subplots(figsize=(12,8))
      sns.barplot(x="total_counts", y="selection", data=rank_df, hue = "grp")
      ax.set_title("Results",fontdict= {'fontsize': 10, 'fontweight':'bold'})
      ax.set_xlabel("Counts")
      ax.set_ylabel("Selection")
      ax.xaxis.label.set_color('white')       
      ax.yaxis.label.set_color('white')
      ax.title.set_color('white')
      ax.tick_params(axis='x', colors='white')   
      ax.tick_params(axis='y', colors='white')
      ax.get_legend().remove()
      st.pyplot(fig)
      
      selected_list=list(rank_df.head(num_candidates)["selection"])
      st.markdown("**Based on the results above, the winners in order are:**")
        
      for i in range(len(selected_list)):
        st.write("Number ", str(i+1), ":", selected_list[i])
          
  else:
       st.error("Please upload a data set with multiple observations")
