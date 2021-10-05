import os
from Compositor import *
import glob
import random
import argparse


def synthesis(opt):
    corpusAddress = opt.corpus_address
    colorBackgrund = opt.color_background
    noise = opt.noise  # 'random'
    composer = Compositor()
    textFileName = os.path.basename(os.path.splitext(corpusAddress)[0])
    fileDict = open("output/gt" + textFileName + ".txt", "a")
    imgsDirectory = "output/imgs" + textFileName

    try:
        os.stat("output")
    except:
        os.mkdir("output")

    try:
        os.stat(imgsDirectory)
    except:
        os.mkdir(imgsDirectory)

    err = 0

    # f = open(txtAddress[i - 1])
    corpus = open(corpusAddress)
    wordList = []
    counter = 1
    while True:
        try:
            line = corpus.readline()
            if not line:
                break
            words = line.split(" ")
            if(words[0] == "ـ" or words[0] == "\n" or words[0] == '،' or words[0] == '.'):
                continue
            word = words[0].replace('\n', '')
            color = (int(random.random() * 255), int(random.random()
                                                     * 255), int(random.random() * 255), 255)
            img = composer.productImage(
                word, colorBackgrund, noise, color, border=3)
            imageAddress = imgsDirectory + "/" + str(counter) + ".png"
            img.save(imageAddress)
            imageLable = imageAddress + "\t"+word+"\n"
            fileDict.write(imageLable)
            fileDict.flush()

            print(imgsDirectory + "/" +
                  str(counter)+".png\t"+word+"\n")
            counter += 1

        except:
            err += 1
            print("error " + str(err))

    print("dataset created by " + str(err) + " max error")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus_address', type=str,
                        help='Where to store corpus', default='text/tabnak1.txt')
    parser.add_argument('--colored_background',
                        dest='color_background', action='store_true')
    parser.add_argument('--image_background',
                        dest='color_background', action='store_false')
    parser.set_defaults(color_background=True)
    # help='Set to synthesised images has color back ground or image background. set True or False', default=False)
    parser.add_argument(
        '--noise', type=str, help='Set type of noise applied on images. use random for use all of noises or set empty', default='random')
    opt = parser.parse_args()
    synthesis(opt)
