import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = st.slider('Pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai',0.0, 10.0, 5.0)
st.write('nilai y:', y)

integration_range = st.slider('Pilih rentang integrasi', x[0], x[1], (x[0], x[1]))
st.write('Rentang Integrasi:', integration_range)

t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
u = np.sin(y*t)

# Calculate f(x) = 9x^2 + 9x - 14
def f(x):
    return 9*x**2 + 9*x - 14

v = f(t)

# Compute integral using trapezoidal rule for u within integration_range
mask_u = (t >= integration_range[0]*np.pi) & (t <= integration_range[1]*np.pi)
integral_u = np.trapz(u[mask_u], t[mask_u])

# Compute integral using trapezoidal rule for v within integration_range
mask_v = (t >= integration_range[0]*np.pi) & (t <= integration_range[1]*np.pi)
integral_v = np.trapz(v[mask_v], t[mask_v])

fig1, ax1 = plt.subplots(figsize=(16, 8))
ax1.plot(t, u, label='sin(t)', color='b')  # Plotting sin(t) curve
ax1.fill_between(t[mask_u], 0, u[mask_u], alpha=0.2, color='b', label='Integral of sin(t)')  # Fill the area under the curve for integral of sin(t)
ax1.set_ylabel("")
ax1.set_xlabel("t")
ax1.tick_params(axis='y', labelsize=20)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=30, ha='right')
ax1.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()  # Show legend for fig1

fig2, ax2 = plt.subplots(figsize=(16, 8))
ax2.plot(t, v, label='f(t)', color='r')     # Plotting f(t) curve
ax2.fill_between(t[mask_v], 0, v[mask_v], alpha=0.2, color='r', label='Integral of f(t)')  # Fill the area under the curve for integral of f(t)
ax2.set_ylabel("")
ax2.set_xlabel("t")
ax2.tick_params(axis='y', labelsize=20)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=30, ha='right')
ax2.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()  # Show legend for fig2

st.pyplot(fig1)
st.pyplot(fig2)

st.write(f'Integral (aturan trapesium) dari sin(t): {integral_u}')
st.write(f'Integral (aturan trapesium) dari sin(t): {integral_v}')
st.write(f'Integral (aturan trapesium) dari sin(t) dalam rentang yang dipilih: {integration_range}: {integral_u}')
st.write(f'Integral (aturan trapesium) dari sin(t) dalam rentang yang dipilih:: {integration_range}: {integral_v}')
