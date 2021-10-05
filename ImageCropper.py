from PIL import Image
import os
import numpy
import glob
import random


class ImageCropper:
    def __init__(self, imageDirectory='UnusedImage', trashDirectory='UsedImage', produceCountLimit=100):
        self._imageDirecotry = imageDirectory
        self._trashDirectory = trashDirectory
        self._imgesAddress = glob.glob(imageDirectory+"/*.jpg")
        self._takePieceCounterLimit = produceCountLimit
        self._takePieceCounter = 0
        self.__loadNewImage()

    def __loadNewImage(self):
        self._takePieceCounter = 0
        while len(self._imgesAddress):
            try:
                self._imageName = self._imgesAddress.pop(0)
                destination = self._imageName.replace(
                    'UnusedImage', 'TempImage')
                os.rename(self._imageName, destination)
                self._imageName = destination
                self._image = Image.open(self._imageName)
                size = self._image.size
                if(size[0] > 200 and size[1] > 200):
                    break
                else:
                    destination = self._imageName.replace(
                        'TempImage', 'BadImages')
                    os.rename(self._imageName, destination)
            except:
                continue
        print(self._imageName)
        if(len(self._imgesAddress)):
            return True
        else:
            return False

    def __generateRandomCadre(self, width, height):
        (imageWidth, imageHeight) = self._image.size
        if(width <= imageWidth and height <= imageHeight):
            startX = random.randrange(0, imageWidth - width + 1, 1)
            startY = random.randrange(0, imageHeight - height + 1, 1)

            endX = startX + width
            endY = startY + height

            return (startX, startY, endX, endY)
        else:

            return (-1, -1, -1, -1)

    def __cropImage(self, bondigBox, border=0):
        image = self._image.crop(bondigBox)
        (width, height) = image.size
        width += border * 2
        height += border * 2

        cropped_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        cropped_image.paste(image, (border, border))

        return cropped_image

    def getImage(self, width, height, coloredImage=False, color=(0, 0, 0, 0)):
        if(coloredImage):
            return self.__getColoredBackgroundImage(width, height, color)

        if(self._takePieceCounter > self._takePieceCounterLimit):
            destination = self._imageName.replace('TempImage', 'UsedImage')
            os.rename(self._imageName, destination)
            hasImage = self.__loadNewImage()
            if(not hasImage):
                print("End of images")
                exit(1)

        self._takePieceCounter += 1
        bondingBox = self.__generateRandomCadre(width, height)
        output = self.__cropImage(bondingBox)

        return output

    def getCurrentImageSize(self):
        return self._image.size

    def __getColoredBackgroundImage(self, width, height, color):
        return Image.new('RGBA', (width, height), color)
