from imgaug import augmenters as iaa
from PIL import Image, ImageOps
from ImageCropper import *
from TextGrapher import *
import numpy as np
import random
import os


class Compositor:
    def __init__(self):
        self._textGrapher = TextGrapher()
        self._imageCropper = ImageCropper()
        self._noise = ['saltAndPeper', 'rotate', 'shear','polarWarping', 'piecewiseAffine']
        self._rotate = iaa.Affine(rotate=(-25, 25))
        self._shear = iaa.Affine(shear=(-25, 25))
        self._piecewiseAffine = iaa.PiecewiseAffine(scale=(0.01, 0.08))
        self._polarWarping= iaa.WithPolarWarping(iaa.CropAndPad(percent=(-0.08, 0.08)))
        self._perspectiveTransform = iaa.PerspectiveTransform(scale=(0.03, 0.5), keep_size=True)

    def __selectRandomNoise(self):
        return random.choice(list(enumerate(self._noise)))

    def __applyNoise(self, image, noise):
        image = np.array(image)
        # rotate = iaa.Affine(rotate=(-25, 25))
        # rotate = iaa.WithPolarWarping(iaa.CropAndPad(percent=(-0.1, 0.1)))
        image_rotated = self._perspectiveTransform.augment_image(image)
        # return image_rotated
        return Image.fromarray(image_rotated)

    def __rotate(self, image):
        return self._rotate.augment_image(image)

    def __shear(self, image):
        return self._shear.augment_image(image)

    def __piecewiseAffine(self, image):
        return self._piecewiseAffine.augment_image(image)

    def __polarWarping(self, image):
        return self._polarWarping.augment_image(image)


    def productImage(self, text, colorBackgrund=False, noise='off', color=(0, 0, 0, 0), border=0, grayScale=True):
        (icW, icH) = self._imageCropper.getCurrentImageSize()

        while True:
            textImage = self._textGrapher.produceTextImage(text, border)
            (width, height) = textImage.size
            if(width < icW and height < icH):
                break

        backImage = self._imageCropper.getImage(
            width, height, colorBackgrund, color)
        colored = Image.alpha_composite(backImage, textImage)
        if(noise != 'off'):
            colored = self.__applyNoise(colored, noise)

        if grayScale:
            gray = ImageOps.grayscale(colored)
            return gray
        else:
            return colored
