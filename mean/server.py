#input a folder name holding shares and an output file name
#output a file with all the provided shares merged

import sys
import os

P = 2**31-1

#check for right number of params
if len(sys.argv) != 3:
    print("wrong number of params!")
    sys.exit()

inFolderName = str(sys.argv[1])
outFileName = str(sys.argv[2])

outputShare = 0
count = 0

#compute the output
myDir = os.getcwd()
inDir = myDir + "/" + inFolderName
for fileName in os.listdir(inDir):
    inFile = open(inDir + "/" + fileName, "r")
    inputBytes = bytes.fromhex(inFile.read())
    inputInt = int.from_bytes(inputBytes, byteorder='big')
    inFile.close()
    #TODO update the outputShare
    count += 1

print("merged "+str(count)+" inputs.")

outputBytes = outputShare.to_bytes(length=4, byteorder='big')

#write the merged share of DB to output file
outFile = open(outFileName, "w")
outFile.write(outputBytes.hex())
outFile.close()
