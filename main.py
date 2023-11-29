
import streamlit as st
import pandas as pd
import IO
st.title('Data visualization')
st.header('Upload file')
data_file = st.file_uploader('Choose a csv file', type=(['.csv']))

if data_file is not None:
 df = pd.read_csv(data_file)

 st.header('Show data')
st.dataframe(df)

st.header('Descriptive staticstics')
st.table(df.describe())

st.header('Show data information')
buffer = io.stringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())
