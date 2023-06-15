#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:09:10 2023
@author: bek
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Define start, interval, count, font_path, output_folder, and invert_colors
start = 0
interval = 3
count = 25
font_path = 'folder_path'  # Update this with the correct path for the font on your system
output_folder = 'output_folder'  # Update this with the desired output folder path
invert_colors = 0  # Set to 0 for white text on black background, or 1 for black text on white background

# Check if output_folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the font
fnt = ImageFont.truetype(font_path, 72)

# Calculate the maximum number to be drawn
max_number = start + interval * (count - 1)

# Calculate the size of the image based on the size of the text of the maximum number
text_width, text_height = fnt.getsize(str(max_number))

# Add a small margin to the size
margin = 10
img_size = max(text_width, text_height) + 2 * margin

# Define text and background colors based on invert_colors
if invert_colors:
    text_color = (0, 0, 0)  # Black text
    background_color = 'white'  # White background
else:
    text_color = (255, 255, 255)  # White text
    background_color = 'black'  # Black background

# Start a loop to generate images
for i in range(count):
    # Calculate the current number
    current_number = start + i * interval

    # Create a new image with specified background color
    img = Image.new('RGB', (img_size, img_size), color = background_color)

    # Create a draw object
    d = ImageDraw.Draw(img)

    # Calculate the position of the text so it's centered horizontally and aligned to the bottom
    text = str(current_number)
    text_width, text_height = d.textsize(text, font=fnt)
    position = ((img_size - text_width) / 2, img_size - text_height - margin)
    
    # Draw the text on the image with specified text color
    d.text(position, text, font=fnt, fill=text_color)

    # Save the image to the output folder
    img.save(f'{output_folder}/number_{i+1}.png')
    print(f"Saved image {i+1}")
