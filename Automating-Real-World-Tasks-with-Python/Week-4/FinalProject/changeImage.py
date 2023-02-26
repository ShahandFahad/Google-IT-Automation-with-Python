#!/usr/bin/env python3
from PIL import Image
import os

images_dir = "supplier-data/images/"

for image in os.listdir(images_dir):
    print(image)
    if image.endswith('.tiff'):
        new_image = Image.open(os.path.join(images_dir, image))
        # print(new_image.size)
        # print(new_image.format)
        
        # TODO: Size: Change image resolution from 3000x2000 to 600x400 pixel
        new_image = new_image.resize((600, 400))
        
        # TODO: Format: Change image format from .TIFF to .JPEG
        
        # JPEG does not support alpha = transparency
        # So before saving to JPEG discard alpha = transparency
        # such as: convert Image to RGB
        # then save to JPEG
        
        new_image = new_image.convert("RGB")
        new_image.save(os.path.join(
            images_dir, image.replace(".tiff", ".jpeg")))
        