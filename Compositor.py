from PIL import Image ,ImageOps
from ImageCropper import *
from TextGrapher import *
import numpy as np
import random
import os

class Compositor:
    def __init__(self):
        self._textGrapher = TextGrapher()
        self._imageCropper = ImageCropper()

    def productImage(self, text, colorBackgrund=False, color=(0, 0, 0, 0), border=0):
        (icW, icH) = self._imageCropper.getCurrentImageSize()

        while True:
            textImage = self._textGrapher.produceTextImage(text, border)
            (width, height) = textImage.size
            if(width < icW and height < icH):
                break

        backImage = self._imageCropper.getImage(
            width, height, colorBackgrund, color)
        colored = Image.alpha_composite(backImage, textImage)
        gray = ImageOps.grayscale(colored)
        return gray
