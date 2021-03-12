import os
from Compositor import *
import glob

textDirectory = "/home/mmt/my thesis/create data set/text/ArmanPersoNERCorpus"
txtAddress = glob.glob(textDirectory+"/*.txt")
print(txtAddress)
composer = Compositor()
while(len(txtAddress) > 0):
    f = open(txtAddress.pop(0))
    while True:
        line = f.readline()
        if not line:
            break
        words = line.split(" ")
        img = composer.productImage(words[0],True)
        img.save("output/"+words[0]+".png")
