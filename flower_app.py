import streamlit as st
from PIL import Image
import turtle

def draw_flower(num_petals, petal_length, petal_width):
    screen = turtle.Screen()
    screen.setup(width=400, height=400)
    screen.tracer(0)  # Disable animation

    flower = turtle.Turtle()
    flower.hideturtle()  # Hide turtle icon

    for _ in range(num_petals):
        flower.circle(petal_length, steps=petal_width)
        flower.left(360 / num_petals)

    screen.update()  # Update the drawing

    canvas = screen.getcanvas()
    canvas.postscript(file="flower.eps")

    # Convert from EPS format to PNG using PIL
    img = Image.open("flower.eps")
    img.save("flower.png")

    screen.bye()  # Close the turtle graphics window
    return "flower.png"

# Streamlit app
st.title('Flower Drawing App')

# User inputs
num_petals = st.slider('Number of Petals', min_value=4, max_value=12, value=6)
petal_length = st.slider('Petal Length', min_value=50, max_value=150, value=100)
petal_width = st.slider('Petal Width', min_value=2, max_value=20, value=10)

if st.button('Draw Flower'):
    flower_image = draw_flower(num_petals, petal_length, petal_width)
    st.image(flower_image)

