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

# Generate t values specifically for the integral calculation range
t_integral = np.linspace(integral_range[0]*np.pi, integral_range[1]*np.pi, 100)
v_integral = f(t_integral)

# Compute integral using trapezoidal rule specifically over the integral range
integral = np.trapz(v_integral, t_integral)

# Plot for sin(yt)
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(t, u, label='sin(yt)', color='b')
ax1.set_ylabel("")
ax1.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()
st.pyplot(fig1)

# Plot for f(t) and highlight the integral area
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.plot(t, v, label='f(t) = 9t^2 + 9t - 14', color='r')

# Ensure that the shaded area for the integral only covers the selected range
# This requires identifying the parts of the t array that fall within the integral range
# and only filling between those limits.
mask = (t >= integral_range[0]*np.pi) & (t <= integral_range[1]*np.pi)
ax2.fill_between(t[mask], 0, v[mask], alpha=0.2, color='r', label='Integral area')
ax2.set_ylabel("")
ax2.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()
st.pyplot(fig2)

# Display the calculated integral value
st.write(f'Integral (using trapezoidal rule over the selected range): {integral}')
