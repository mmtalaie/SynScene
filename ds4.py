import os
from Compositor import *
import glob
import random

i = 4
textDirectory = "text/ArmanPersoNERCorpus"
txtAddress = glob.glob(textDirectory+"/*.txt")
print(txtAddress)
composer = Compositor()
fileDict = open("output/gt" + str(i) + ".txt", "a")
imgsDirectory = "output/imgs" + str(i)

try:
    os.stat("output")
except:
    os.mkdir("output")


try:
    os.stat(imgsDirectory)
except:
    os.mkdir(imgsDirectory)


a = 53455

f = open(txtAddress[i - 1])
while True:
    line = f.readline()
    if not line:
        break
    words = line.split(" ")
    if(words[0] == "ـ" and words[0] == "\n"):
        continue
    color = (int(random.random() * 255), int(random.random()
                                             * 255), int(random.random() * 255), 255)
    img = composer.productImage(words[0], True, 'random', color, border=3)
    img.save(imgsDirectory + "/word"+str(i)+"_" + str(a) + ".png")
    fileDict.write(imgsDirectory + "/word"+str(i) +
                   "_" + str(a)+".png\t"+words[0]+"\n")
    fileDict.flush()
    a += 1
    print(imgsDirectory + "/word"+str(i)+"_" + str(a)+".png\t"+words[0]+"\n")
