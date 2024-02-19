import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_flower(num_petals, radius):
    theta = np.linspace(0, 2*np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig, ax = plt.subplots()
    for i in range(num_petals):
        ax.plot(x*np.cos(i*2*np.pi/num_petals) - y*np.sin(i*2*np.pi/num_petals),
                x*np.sin(i*2*np.pi/num_petals) + y*np.cos(i*2*np.pi/num_petals), 
                color='pink')
    ax.set_aspect('equal')
    st.pyplot(fig)

st.title('Flower Generator')

num_petals = st.slider('Number of Petals:', 4, 20, 8)
radius = st.slider('Radius:', 1, 10, 5)

if st.button('Draw Flower'):
    draw_flower(num_petals, radius)
