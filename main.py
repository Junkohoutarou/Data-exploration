import streamlit as st
st.title('Data visualization')
data_file = st.file_uploader('Choose a csv file', type=(['.csv']))

if data_file is not none
 df = pd.read_csv(data_file)

 st.datafame(df)
 
