import os
corpusAddress = "text/tabnak.txt"
corpus = open(corpusAddress)
corpusName = os.path.basename(os.path.splitext(corpusAddress)[0])
divisionSize = 100000

rootAddress = "text/"

endFile = False
count = 1
while not endFile:
    division = open(rootAddress + "/" + corpusName + str(count) + ".txt", "a")
    count += 1
    for i in range(divisionSize):
        line = corpus.readline()
        if not line:
            endFile = True
            break
        division.write(line)
    division.flush()
