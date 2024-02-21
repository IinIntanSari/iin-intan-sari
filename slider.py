import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Selecting the range with a slider.
x = st.slider('Pilih rentang', 0.0, 2.0, (0.2, 0.5))
st.write('nilai x:', x)

# Another slider, not used in the plotting of f(x) or sin(t).
y = st.slider('Set nilai', 0.0, 100.0, 25.0)
st.write('nilai y:', y)

# Generating values for t.
t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
# Sine function.
u = np.sin(t)

# New function f(x) = 9x^2 + 9x - 14.
f_x = 9 * t**2 + 9 * t - 14

# Plot setup.
fig, ax = plt.subplots(figsize=(16, 8))

# Plotting sin(t).
ax.plot(t, u, label='sin(t)', color='b')

# Plotting f(x) = 9x^2 + 9x - 14.
ax.plot(t, f_x, label='9x^2 + 9x - 14', color='r')

# Plot adjustments.
ax.set_ylabel("y")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
# Correcting the method to set x-tick labels.
plt.xticks(rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()

# Calculating the trapezoidal integral of f(x).
integral_fx = np.trapz(f_x, t)
# Displaying the integral result.
st.write(f"Integral trapesium dari f(x) = 9x^2 + 9x - 14 dari {x[0]*np.pi:.2f} hingga {x[1]*np.pi:.2f} adalah {integral_fx:.2f}")

st.pyplot(fig)
