import os
import random
datasetAddress = "text/number/phoneNumber.txt"
dataset = open(datasetAddress, "a")
preNumber = ['0936', '0917', '0912', '0919', '0901', '0935', '0933',
             '0915', '0916', '0913', '0920', '0938', '0939', '0990', '0910', '0914']

for i in range(0, 100000):
    preNumIndex = random.randint(0, 15)
    line = preNumber[preNumIndex]
    space = random.random()
    for j in range(0, 7):
        if(space > 0.5):
            if(j == 0 or j == 3 or j == 5):
                line += ' '
        line += str(random.randint(0, 9))

    dataset.write(line + '\n')
dataset.flush()
