import os
from Compositor import *
import glob
import random

textDirectory = "text/ArmanPersoNERCorpus"
txtAddress = glob.glob(textDirectory+"/*.txt")
print(txtAddress)
composer = Compositor()
fileDict = open("output/gt1.txt", "a")
ingsDirectory = "output/imgs1"
try:
    os.stat(ingsDirectory)
except:
    os.mkdir(ingsDirectory)
a = 0
while(len(txtAddress) > 0):
    f = open(txtAddress.pop(0))
    while True:
        line = f.readline()
        if not line:
            break
        words = line.split(" ")
        if(words[0] == "ـ"):
            continue
        color = (int(random.random() * 255), int(random.random()
                 * 255), int(random.random() * 255), 255)
        img = composer.productImage(words[0], True, color, border=3)
        img.save(ingsDirectory + "/word_" + str(a) + ".png")
        fileDict.write(ingsDirectory + "/word_"+str(a)+".png\t"+words[0]+"\n")
        fileDict.flush()
        a += 1
        print("imgs/word_"+str(a)+".png\t"+words[0]+"\n")
