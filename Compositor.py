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
        # self._noise = ['saltAndPeper', 'rotate', 'shear', 'polarWarping',
        #                'piecewiseAffine', 'clahe', 'perspectiveTransform']
        self._noise = ['saltAndPeper', 'rotate', 'shear',
                       'piecewiseAffine', 'clahe', 'perspectiveTransform']
        self._rotate = iaa.Affine(rotate=(-25, 25))
        self._shear = iaa.Affine(shear=(-25, 25))
        self._piecewiseAffine = iaa.PiecewiseAffine(scale=(0.01, 0.04))
        self._polarWarping = iaa.WithPolarWarping(
            iaa.CropAndPad(percent=(-0.08, 0.08)))
        self._perspectiveTransform = iaa.PerspectiveTransform(
            scale=(0.03, 0.05), keep_size=True)
        self._saltAndPeper = iaa.SaltAndPepper(
            p=(0.03, 0.07), per_channel=False)
        self._clahe = iaa.CLAHE(tile_grid_size_px=(3, 21))

    def __selectRandomNoise(self):
        return random.choice(list(enumerate(self._noise)))

    def __applyNoise(self, image, noise):
        print("noise = " + noise)
        image = np.array(image)
        if('saltAndPeper' in noise):
            image_noisy = self._saltAndPeper.augment_image(image)
        if('rotate' in noise):
            image_noisy = self._rotate.augment_image(image)
        if('shear' in noise):
            image_noisy = self._shear.augment_image(image)
        if('polarWarping' in noise):
            image_noisy = self._polarWarping.augment_image(image)
        if('piecewiseAffine' in noise):
            image_noisy = self._piecewiseAffine.augment_image(image)
        if('clahe' in noise):
            image_noisy = self._clahe.augment_image(image)
        if('perspectiveTransform' in noise):
            image_noisy = self._perspectiveTransform.augment_image(image)
        return Image.fromarray(image_noisy)

    def __rotate(self, image):
        return self._rotate.augment_image(image)

    def __shear(self, image):
        return self._shear.augment_image(image)

    def __piecewiseAffine(self, image):
        return self._piecewiseAffine.augment_image(image)

    def __polarWarping(self, image):
        return self._polarWarping.augment_image(image)

    def __perspectiveTransform(self, image):
        return self._perspectiveTransform.augment_image(image)

    def __saltAndPeper(self, image):
        return self._saltAndPeper.augment_image(image)

    def __clahe(self, image):
        return self._clahe.augment_image(image)

    def __getCountOfNoiseByChanse(self) -> int:
        return random.randrange(0, 4)

    def __generateRandomNoiseOrder(self, count):
        c = count
        noiseOrd = ''
        while(c > 0):
            newNoise = self.__selectRandomNoise()[1]
            if(newNoise not in noiseOrd):
                if (noiseOrd == ''):
                    noiseOrd = newNoise
                else:
                    noiseOrd = '{}-{}'.format(noiseOrd, newNoise)
                c -= 1

        return noiseOrd

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

        if(noise == 'random'):
            noiseCount = self.__getCountOfNoiseByChanse()
            if(noiseCount > 0):
                noiseInstruction = self.__generateRandomNoiseOrder(noiseCount)
                print('noises = ' + noiseInstruction)
                singleInstructions = noiseInstruction.split('-')
                for instruction in singleInstructions:
                    colored = self.__applyNoise(colored, instruction)

        if grayScale:
            gray = ImageOps.grayscale(colored)
            return gray
        else:
            return colored
