from PIL import Image
import numpy
import glob
import random

class ImageCropper:
    def __init__(self, imageDirectory='./UnusedImage', trashDirectory='./UsedImage', produceCountLimit=100):
        self._imageDirecotry = imageDirectory
        self._trashDirectory = trashDirectory
        self._imgesAddress = glob.glob(imageDirectory+"/*.jpg")
        self._takePieceCounterLimit = produceCountLimit
        self._takePieceCounter = 0
        self._loadNewImage()

    def _loadNewImage(self):
        self._takePieceCounter = 0
        if(len(self._imgesAddress)):
            self._image = Image.open(self._imgesAddress.pop(0))
            print(self._image)

            return True
        else:

            return False

    def _generateRandomCadre(self, width, height):
        (imageWidth, imageHeight) = self._image.size
        if(width <= imageWidth and height <= imageHeight):
            startX = random.randrange(0, imageWidth - width + 1, 1)
            startY = random.randrange(0, imageHeight - height + 1, 1)

            endX = startX + width
            endY = startY + height

            return (startX, startY, endX, endY)
        else:

            return (-1, -1, -1, -1)

    def _cropImage(self, bondigBox, border=0):
        image = self._image.crop(bondigBox)
        (width, height) = image.size
        width += border * 2
        height += border * 2

        cropped_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        cropped_image.paste(image, (border, border))

        return cropped_image

    def getImage(self, width, height):
        if(self._takePieceCounter > self._takePieceCounterLimit):
           hasImage = self._loadNewImage()
           if(not hasImage):
               print ("End of images")
               exit(1)

        self._takePieceCounter += 1
        bondingBox = self._generateRandomCadre(width, height)
        output = self._cropImage(bondingBox)
        
        return output

    def getCurrentImageSize(self):
        return self._image.size
        