from PIL import Image
from ImageCropper import *
from TextGrapher import *
import numpy as np
import random
import os


class Compositor:
    def __init__(self):
        self._textGrapher = TextGrapher()
        self._imageCropper = ImageCropper()

    def productImage(self, text, colorBackgrund=False, color=(0, 0, 0, 0)):
        while True:
            textImage = self._textGrapher.produceTextImage(text)
            (width, height) = textImage.size
            (icW, icH) = self._imageCropper.getCurrentImageSize()
            if(width < icW and height < icH):
                break

        backImage = self._imageCropper.getImage(
            width, height, colorBackgrund, color)

        return Image.alpha_composite(backImage, textImage)
