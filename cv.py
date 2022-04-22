import numpy as np
from PIL import Image
import warnings
from tkinter import *




def processing(img):
    pix = 0
    arr = np.asarray(img.convert('RGB'))
    found_second = True
    data = np.array([255, 0, 0])
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if all(arr[i][j] == data):
                if found_second:
                    found_second = False
                else:
                    found_second = True
            if not found_second:
                pix += 1

    root = Tk()

    canvas = Canvas(root, width=100, height=100)
    canvas.pack()
    canvas.create_text(50, 50, text=str(pix) + 'p', fill='red')

