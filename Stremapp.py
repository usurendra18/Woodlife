import streamlit as st
import pandas as pd

DATA_PATH = "C://Users//91964//myproject//Candiour 40.xlsx"
df = pd.read_excel(DATA_PATH)

# Filters
search_query = st.text_input("Search by Name or Mobile")
flag_filter = st.selectbox("Select Flag", options=["", "Y", "N"], index=0)

# Apply filters
filtered_df = df.copy()
if search_query:
    filtered_df = filtered_df[
        filtered_df["NAME"].str.contains(search_query, case=False, na=False)
        | filtered_df["NUMBER"].astype(str).str.contains(search_query)
    ]
if flag_filter:
    filtered_df = filtered_df[filtered_df["Flag"].astype(str) == flag_filter]

# Display results
st.write(f"Total Rows: {len(filtered_df)}")
st.dataframe(filtered_df)
