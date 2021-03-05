from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
import numpy as np
import random
import os


class TextGrapher:
    def __init__(self):
        self._fonts = os.listdir('fonts/')

        self._direction = ['rtl', 'utd']

        self._noise = ['none', 'saltAndPeper']

        self._color = (0, 0, 0, 0)

        self._fontSize = 10

        self._opacity = 200

        self._angle = 0

    def __selectRandomColor(self):
        self._color = (int(random.random() * 255),
                       int(random.random() * 255), int(random.random() * 255), 255)
        return self._color

    def __selectRandomFont(self):
        return random.choice(list(enumerate(self._fonts)))

    def __selectRandomNoise(self):
        return random.choice(list(enumerate(self._noise)))

    def __selectRandomDirection(self):
        return random.choice(list(enumerate(self._direction)))

    def __randomOpacity(self, first=200, last=255, step=1):
        return random.randrange(first, last+1, step)

    def __useRandomOpacity(self):
        return bool(random.randrange(0, 2, 1))

    def __randomSize(self, first=10, last=36, step=1):
        return random.randrange(first, last+1, step)

    def __randomAngle(self, first=0, last=10, step=1):
        return random.randrange(first, last+1, step)

    def __selectTextCadre(self, image):
        width, height = image.size
        startX = width
        endX = 0
        startY = height
        endY = 0
        for i in range(0, width):
            for j in range(0, height):
                r, g, b, a = image.getpixel((i, j))
                if(a > 0):
                    if(i < startX):
                        startX = i
                    if(j < startY):
                        startY = j
                    if(i > endX):
                        endX = i
                    if(j > endY):
                        endY = j

        return startX, startY, endX, endY

    def __autocropImage(self, image, bondigBox, border=0):
        # Get the bounding box
        # bbox = image.getbbox()

        # Crop the image to the contents of the bounding box
        image = image.crop(bondigBox)

        # Determine the width and height of the cropped image
        (width, height) = image.size

        # Add border
        width += border * 2
        height += border * 2

        # Create a new image object for the output image
        cropped_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # Paste the cropped image onto the new image
        cropped_image.paste(image, (border, border))

        # Done!
        return cropped_image

    def produceTextImage(self, text="سلام"):
        color = self.__selectRandomColor()
        backgroundColor = (color[0], color[1], color[2], 0)
        size = self.__randomSize(80, 150, 1)
        image = Image.new('RGBA', (size * 10, size * 10), backgroundColor)
        draw = ImageDraw.Draw(image)

        wrapped = textwrap.fill(text)

        if (self.__useRandomOpacity):
            fontColor = (color[0], color[1], color[2], self.__randomOpacity())
        else:
            fontColor = color

        print(F"text opacity = {fontColor[3]}")

        unicodeFont = ImageFont.truetype(
            f"./fonts/{self.__selectRandomFont()[1]}", size)

        draw.text((100, 100), wrapped, spacing=30, font=unicodeFont,
                  fill=fontColor, direction='rtl', align='left')

        bbox = (self.__selectTextCadre(image))
        cruppedImage = self.__autocropImage(image, bbox)

        foreground = Image.new('RGBA', cruppedImage.size, color)
        foreground.paste(cruppedImage)

        return foreground
