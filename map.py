import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import os
import random

# Function to create a map frame with highlighted grids and save it as a PNG
def create_map_frame(grid_indices, total_grids, frame_number, map_image):
    fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
    
    ax.imshow(map_image)
    ax.set_xlim(0, map_image.shape[1])
    ax.set_ylim(map_image.shape[0], 0)
    ax.axis('off')
    
    # Highlight the current grids
    grid_size_x = map_image.shape[1] / total_grids
    grid_size_y = map_image.shape[0] / total_grids
    for index in grid_indices:
        x_start = (index % total_grids) * grid_size_x
        y_start = (index // total_grids) * grid_size_y
        rect = plt.Rectangle((x_start, y_start), grid_size_x, grid_size_y, linewidth=2, edgecolor='red', facecolor='none')
        ax.add_patch(rect)
    
    # Save frame as PNG
    frame_path = f"map_frame_{frame_number:03d}.png"
    plt.savefig(frame_path, bbox_inches='tight')
    plt.close(fig)
    return frame_path

# Load map image
map_image_path = 'images/Fancy Blank Map.png'
map_image = np.array(Image.open(map_image_path))

# Parameters
total_grids = 5
num_combinations = 10  # Number of combinations to show

# Create random grid combinations
all_grids = list(range(total_grids * total_grids))
combinations = [random.sample(all_grids, k=random.randint(1, total_grids)) for _ in range(num_combinations)]

# Create map frames
map_frame_paths = []
for i, combination in enumerate(combinations):
    map_frame_path = create_map_frame(combination, total_grids, i, map_image)
    map_frame_paths.append(map_frame_path)

# Create map GIF
map_frames = [Image.open(frame) for frame in map_frame_paths]
map_frames[0].save('map_grid_animation.gif', save_all=True, append_images=map_frames[1:], duration=1000, loop=0)

# Clean up temporary map frame files
for map_frame_path in map_frame_paths:
    os.remove(map_frame_path)
