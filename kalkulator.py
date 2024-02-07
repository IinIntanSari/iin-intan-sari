import streamlit as st

# Header
st.header('Intan :sparkles:')

# Subheader
st.subheader('Kalkulator')

# Membuat tiga kolom
c1, c2, c3 = st.columns(3)

# Kolom pertama
with c1:
  num1 = st.number_input('Masukkan angka pertama', step=1)
 
with c2:
  # pilih operasi
  operation = st.selectbox('pilih operasi', ('+', '-', 'x', '/'))

# Kolom ketiga
with c3:
  num2 = st.number_input('Masukkan angka kedua', step=1)

def calculate(num1, num2, operation):
  if operation == '+':
    result = num1 + num2
  elif operation == '-':
    result = num1 - num2
  elif operation == 'x':
     result = num1 * num2
  elif operation == '/':
    if num2 != 0: # Menghindari pembagian dengan nol
      result = num1 / num2
    else:
      result = "Error: Pembagian dengan nol"
      return result

result = calculate(num1, num2, operation)
st.write('Hasil:' result)

st.caption('copyright © Iin Intan Insari 2024')


