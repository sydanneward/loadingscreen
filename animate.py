import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
import os

# Function to create a single frame and save it as a PNG
def create_frame(position, total_cows, frame_number, earth_image, moon_image, cow_image):
    fig, ax = plt.subplots(figsize=(12, 4), dpi=100)
    
    ax.set_xlim(0, total_cows + 4)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    
    # Draw Earth
    ax.imshow(earth_image, extent=[0, 2, -1, 1])
    
    # Draw Moon
    ax.imshow(moon_image, extent=[total_cows + 2, total_cows + 4, -1, 1])
    
    # Calculate the space between the Earth and the Moon
    start_pos = 2
    end_pos = total_cows + 2
    cow_step = (end_pos - start_pos) / (total_cows + 1)  # Adjusted to fit within bounds
    
    # Draw cows stacking horizontally
    for i in range(position + 1):
        ax.imshow(cow_image, extent=[start_pos + i * cow_step, start_pos + (i + 1) * cow_step, -0.5, 0.5])
    
    # Save frame as PNG
    frame_path = f"frame_{frame_number:03d}.png"
    plt.savefig(frame_path)
    plt.close(fig)
    return frame_path

# Load PNG images
def load_image(image_path):
    return np.array(Image.open(image_path))

# Parameters
total_cows = 10
total_frames = total_cows + 10

# Define the paths to the images in the subfolder
earth_image_path = 'images/Untitled-1.png'
moon_image_path = 'images/Untitled-1-02.png'
cow_image_path = 'images/Untitled-1-03.png'

# Load the images
earth_image = load_image(earth_image_path)
moon_image = load_image(moon_image_path)
cow_image = load_image(cow_image_path)

# Create frames
frame_paths = []
for i in range(total_frames):
    frame_path = create_frame(min(i, total_cows), total_cows, i, earth_image, moon_image, cow_image)
    frame_paths.append(frame_path)

# Create GIF
frames = [Image.open(frame) for frame in frame_paths]
frames[0].save('cow_stack.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)

# Clean up temporary frame files
for frame_path in frame_paths:
    os.remove(frame_path)
