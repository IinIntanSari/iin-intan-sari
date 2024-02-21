import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Slider for selecting the range for t.
x = st.slider('Pilih rentang', 0.0, 2.0, (0.2, 0.5))
st.write('Nilai x:', x)

# Slider for a fixed value y (not directly used in plotting f(x) or sin(t)).
y = st.slider('Set nilai', 0.0, 100.0, 25.0)
st.write('Nilai y:', y)

# Generating the values for t and the sine wave.
t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
u = np.sin(t)

# Calculating the values for f(x) = 9x^2 + 14x - 9.
f_x = 9 * t**2 + 14 * t - 9

# Computing the integral using the trapezoidal rule.
integral_sin = np.trapz(u, t)
integral_fx = np.trapz(f_x, t)

# Creating the plot.
fig, ax = plt.subplots(figsize=(16, 8))

# Plotting the sine wave.
ax.plot(t, u, label='sin(t)', color='b')

# Plotting the function f(x) = 9x^2 + 14x - 9.
ax.plot(t, f_x, label='9x^2 + 14x - 9', color='r')

ax.set_ylabel("y")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=30)  # Rotates the x-axis tick labels to make them more readable.

plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()
st.pyplot(fig)

# Displaying the results of the integrals.
st.write(f'Integral of sin(t) over the range: {integral_sin:.2f}')
st.write(f'Integral of 9x^2 + 14x - 9 over the range: {integral_fx:.2f}')


