import numpy as np
import matplotlib.pyblot as plt
import streamlit as st

# Header
st.header('IinIntan : sparkles :')
st.subheader('Plot')

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000) # Generating x values from -2*
y = np.sin(x) # Calculating sin(x) values
z = np.cos(x) # Calculating sin(x) values

fig, ax = plt.sublots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b') # plotting sin(x) curve
ax.plot(x, z, label='cos(x)', color='g') # plotting sin(x) curve
ax.set_ylabel("")
ax.set_ylabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.tick_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis'x', labelsize=15)

st.pyplot(fig)

#subheader
st.subheader("Plot Sin & cos")

with co11:
  st.caption('Plot Sin')
  x = np.linspace(-2 * np.pi, 2 * np.pi, 1000) # Generating x values from -2*pi
  y = np.cos(x) # Calculating sin(x) values

fig, ax = plt.sublots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b') # plotting sin(x) curve
ax.set_ylabel("sin x")
ax.set_ylabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis'x', labelsize=15)

st.pyplot(fig)


with col2:
  x = np.linspace(-2 * np.pi, 2 * np.pi, 1000) # Generating x values from -2*
  y = np.cos(x) # Calculating sin(x) values

fig, ax = plt.sublots(figsize=(16, 8))
ax.plot(x, y, label='cos(x)', color='g') # plotting cos(x) curve
ax.set_ylabel("cos x")
ax.set_ylabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis'x', labelsize=15)

st.pyplot(fig)

st.caption('copyright = IIN INTAN INSAEI 2024')
