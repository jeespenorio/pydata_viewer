import pandas as pd
import streamlit as st

# Specify the actual path to your Excel file
excel_file_path = r'C:\Users\User\Desktop\sample\October 8 to October 14\Analyze Data\merged-files.csv'

# Get the available sheet names
excel_file = pd.ExcelFile(excel_file_path)
sheet_names = excel_file.sheet_names

st.title("Excel Sheet Viewer")

for sheet_name in sheet_names:
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    st.markdown(f"**Selected Sheet:** {sheet_name}")
    st.write(df)
