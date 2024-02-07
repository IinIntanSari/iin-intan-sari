import streamlit as st

# Header
st.header('Intan :sparkles:')
st.subheader('plot')

c1, c2 = st.columns(2)

with c1:
  x = st.number_input('suhu ',value=100)
  st.write('=>: ')
with c2:
  satuan = st.selectbox(
    'Satuan'
    ('C', 'F', 'R', 'K'),key='k1')

st.write(x,' ',satuan,' = ',' ')
st.caption('copyright * Iin Intan Insari 2023')
