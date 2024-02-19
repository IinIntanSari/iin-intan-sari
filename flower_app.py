import matplotlib.pyplot as plt
import numpy as np

def draw_petal(ax, radius=1, angle=0, color='lightblue'):
    # Membuat data untuk kelopak bunga
    theta = np.linspace(0, 2*np.pi, 100)
    r = radius * np.cos(4*theta)  # Formula untuk kelopak bunga
    
    # Mengubah koordinat polar ke koordinat kartesian
    x = r * np.cos(theta + angle)
    y = r * np.sin(theta + angle)
    
    # Menggambar kelopak
    ax.fill(x, y, color=color, zorder=1)

def draw_flower(num_petals=6):
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    
    # Menggambar setiap kelopak
    for i in range(num_petals):
        draw_petal(ax, angle=i*2*np.pi/num_petals)
    
    # Menggambar inti bunga
    circle = plt.Circle((0, 0), 0.2, color='yellow', zorder=2)
    ax.add_artist(circle)
    
    plt.axis('off')  # Menyembunyikan sumbu
    plt.show()

# Menggambar bunga dengan jumlah kelopak tertentu
draw_flower(num_petals=8)
