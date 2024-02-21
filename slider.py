import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define sliders in the Streamlit app
x = st.slider('Pilih rentang untuk plot', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai', 0.0, 10.0, 5.0)
st.write('nilai y:', y)

# Add a slider for selecting the integral calculation range
integral_range = st.slider('Pilih rentang untuk integral', 0.0, 2.0, (.2, .5))
st.write('Rentang integral:', integral_range)

# Generate t values for the plot
t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
u = np.sin(y*t)

# Define the function f(x)
def f(x):
    return 9*x**2 + 9*x - 14

v = f(t)

# Compute integral using trapezoidal rule specifically over the integral range
t_integral = np.linspace(integral_range[0]*np.pi, integral_range[1]*np.pi, 100)
v_integral = f(t_integral)
integral_selected_range = np.trapz(v_integral, t_integral)

# Compute the total integral over the full range (0 to 2π)
t_full = np.linspace(0, 2*np.pi, 1000)
v_full = f(t_full)
integral_full_range = np.trapz(v_full, t_full)

# Plot for sin(yt) with shaded integral range
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(t, u, label='sin(yt)', color='b')
ax1.fill_between(t_integral, np.sin(y*t_integral), color='gray', alpha=0.3)
ax1.set_ylabel("")
ax1.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()
st.pyplot(fig1)

# Plot for f(t) and highlight the integral area
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.plot(t, v, label='f(t) = 9t^2 + 9t - 14', color='r')
ax2.fill_between(t_integral, 0, v_integral, alpha=0.2, color='r', label='Integral area')
ax2.set_ylabel("")
ax2.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()
st.pyplot(fig2)

# Display the calculated integral value
st.write(f'Integral over selected range (using trapezoidal rule): {integral_selected_range}')
st.write(f'Total integral over full range (0 to 2π): {integral_full_range}')

