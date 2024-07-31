import streamlit as st
import pandas as pd

from utils import calculate_sus

df_sus_template = pd.read_excel("sus_template.xlsx");


st.markdown("# Sus Calculator")

st.markdown("## Format of the file")
st.markdown("Each of the question of the SUS questionnaire are numeroted from 1 to 10 as you can see on this page https://www.guillaumegronier.com/cv/blog/files/6545bc93a9d0952c2afac2581129ae7c-0.html.")
st.markdown("The first row of your Excel file needs to be each digit. You can see a blank well-formatted example just below.")

st.dataframe(df_sus_template)

# file uploader to receive the excel file
file = st.file_uploader("SUS questionnaire results", type=["xlsx"])

if file is not None:
    sus = pd.read_excel(file)
    st.write(sus)

    # result of the sus calculation
    sus_result = calculate_sus(sus)
    st.write(f"Result of your SUS questionnaire: {sus_result}/100")
