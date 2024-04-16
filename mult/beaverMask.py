#input 2 share files, a beaver triple file, and output file name
#output a file containing 2 input shares masked with shares of a, b from the beaver triple file

import sys
import os
import math

#biggest prime that fits in 31 bits
#useful resource: https://t5k.org/lists/2small/
P = 2**31-1


#check for right number of params
if len(sys.argv) != 5:
    print("wrong number of params!")
    sys.exit()

xFileName = str(sys.argv[1])
yFileName = str(sys.argv[2])
beaverFileName = str(sys.argv[3])
outFileName = str(sys.argv[4])

xFile = open(xFileName, "r")
yFile = open(yFileName, "r")
beaverFile = open(beaverFileName, "r")

xBytes = bytes.fromhex(xFile.read())
yBytes = bytes.fromhex(yFile.read())

aBytes = bytes.fromhex(beaverFile.readline())
bBytes = bytes.fromhex(beaverFile.readline())

x = int.from_bytes(xBytes, byteorder='big') % P
y =  int.from_bytes(yBytes, byteorder='big') % P

a = int.from_bytes(aBytes, byteorder='big') % P
b = int.from_bytes(bBytes, byteorder='big') % P

out1 = x - a
if out1 < 0:
	out1 = P + out1
	
out2 = y - b
if out2 < 0:
	out2 = P + out2

out1Bytes = out1.to_bytes(length=4, byteorder='big')
out2Bytes = out2.to_bytes(length=4, byteorder='big')
	
outFile = open(outFileName, 'w')

outFile.writelines([out1Bytes.hex()+"\n", out2Bytes.hex()+"\n"])

outFile.close()
