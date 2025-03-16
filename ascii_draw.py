import cv2
import numpy as np
import time
import os
import sys
from colorama import init, Fore, Back
from tkinter import Tk, filedialog

init()

ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image_path, width=150):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Path gambar bener ga?")
        return []
    
    aspect_ratio = img.shape[1] / img.shape[0]
    height = int(width / aspect_ratio * 0.5)  
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)

    scale_factor = 255 / (len(ASCII_CHARS) - 1)
    ascii_image = [[ASCII_CHARS[int(pixel / scale_factor)] for pixel in row] for row in img]
    return ascii_image

def draw_ascii(ascii_image, delay=0.0001):
    os.system("color F0")
    os.system("cls" if os.name == "nt" else "clear")

    for row in ascii_image:
        for char in row:
            sys.stdout.write(Fore.BLACK + Back.WHITE + char + Fore.RESET + Back.RESET)  
            sys.stdout.flush()
            time.sleep(delay)  
        print()  

if __name__ == "__main__":
    Tk().withdraw()
    image_path = filedialog.askopenfilename(title="Pilih gambar", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if image_path:
        ascii_art = image_to_ascii(image_path)
        
        if ascii_art:
            draw_ascii(ascii_art)
    else:
        print("Tidak ada gambar yang dipilih.")
