import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import os

# Function to create an icon frame with filling animation
def create_icon_frame(icon_index, total_icons, frame_number, icon_images, filled_icon_images):
    fig, ax = plt.subplots(figsize=(8, 2), dpi=100)
    
    ax.set_xlim(0, total_icons * 3)
    ax.set_ylim(0, 3)
    ax.axis('off')
    
    # Draw icons and fill them sequentially
    for i in range(total_icons):
        if i <= icon_index:
            ax.imshow(filled_icon_images[i], extent=[i * 3, (i + 1) * 3, 0, 3])
        else:
            ax.imshow(icon_images[i], extent=[i * 3, (i + 1) * 3, 0, 3])
    
    # Save frame as PNG
    frame_path = f"icon_frame_{frame_number:03d}.png"
    plt.savefig(frame_path)
    plt.close(fig)
    return frame_path

# Load icon images
def load_image(image_path):
    return np.array(Image.open(image_path))

# Parameters
total_icons = 4
total_frames = total_icons * 10

# Define the paths to the icon images in the subfolder
icon_image_paths = [
    'static/images/cow.png',
    'static/images/cow.png',
    'static/images/cow.png',
    'static/images/cow.png',
]

filled_icon_image_paths = [
    'static/images/cow (1).png',
    'static/images/cow (1).png',
    'static/images/cow (1).png',
    'static/images/cow (1).png',
]

# Load the images
icon_images = [load_image(path) for path in icon_image_paths]
filled_icon_images = [load_image(path) for path in filled_icon_image_paths]

# Create icon frames
icon_frame_paths = []
for i in range(total_frames):
    icon_index = i // 10  # Fill one icon every 10 frames
    icon_frame_path = create_icon_frame(icon_index, total_icons, i, icon_images, filled_icon_images)
    icon_frame_paths.append(icon_frame_path)

# Create icon GIF
icon_frames = [Image.open(frame) for frame in icon_frame_paths]
icon_frames[0].save('icon_fill_animation.gif', save_all=True, append_images=icon_frames[1:], duration=100, loop=0)

# Clean up temporary icon frame files
for icon_frame_path in icon_frame_paths:
    os.remove(icon_frame_path)
