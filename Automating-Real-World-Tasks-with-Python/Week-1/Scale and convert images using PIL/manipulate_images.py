#!/usr/bin/env python3

from PIL import Image
import os

images_dir = "images/"
output_dir = "/opt/icons/"

# loop over each file in images dir and modify it

for image in os.listdir(images_dir):
    if image != ".DS_Store":
        new_image = Image.open(os.path.join(images_dir, image))
        new_image = new_image.rotate(90)
        new_image = new_image.resize((128, 128))

        # JPEG does not support alpha = transparency
        # So before saving to JPEG discard alpha = transparency
        # such as: convert Image to RGB
        # then save to JPG

        new_image = new_image.convert("RGB")
        new_image.save(os.path.join(
            output_dir, image + ".jpeg"))
