#input shares of x, y, a file containing two masked shares from the other party, a beaver triple share, an output file name, and an input 1 or 2 indicating whether this is the party holding share 1 or share 2 of the messages
#outputs share of product

import sys
import os
import math

#biggest prime that fits in 31 bits
#useful resource: https://t5k.org/lists/2small/
P = 2**31-1

xFileName = str(sys.argv[1])
yFileName = str(sys.argv[2])
maskedFileName = str(sys.argv[3])
beaverFileName = str(sys.argv[4])
outFileName = str(sys.argv[5])

partyNum = int(sys.argv[6])

#check for right number of params
if len(sys.argv) != 7:
    print("wrong number of params!")
    sys.exit()
    
xFile = open(xFileName, "r")
yFile = open(yFileName, "r")
maskedFile = open(maskedFileName, "r")
beaverFile = open(beaverFileName, "r")

#read in the inputs
xBytes = bytes.fromhex(xFile.read())
yBytes = bytes.fromhex(yFile.read())
x = int.from_bytes(xBytes, byteorder='big') % P
y =  int.from_bytes(yBytes, byteorder='big') % P

e_0Bytes = bytes.fromhex(maskedFile.readline())
d_0Bytes = bytes.fromhex(maskedFile.readline())
e_0 = int.from_bytes(e_0Bytes, byteorder='big') % P
d_0 = int.from_bytes(d_0Bytes, byteorder='big') % P

aBytes = bytes.fromhex(beaverFile.readline())
bBytes = bytes.fromhex(beaverFile.readline())
cBytes = bytes.fromhex(beaverFile.readline())
a = int.from_bytes(aBytes, byteorder='big') % P
b = int.from_bytes(bBytes, byteorder='big') % P
c = int.from_bytes(cBytes, byteorder='big') % P

#compute the other half of the masked values
e_1 = x - a
if e_1 < 0:
	e_1 = P + e_1
d_1 = y - b
if d_1 < 0:
	d_1 = P + d_1
	
#TODO compute the merged masked values e and d
e = (e_0 + e_1) % P
d = (d_0 + d_1) % P

#TODO compute z
z = (c + (x * d) + (y * e)) % P

#NOTE: this code handles the -ed/2 part of computing z for you, so you can skip that part.
if partyNum == 1:
	ed = e*d % P
	z = z - ed
	if z < 0:
		z = P + z
		
outBytes = z.to_bytes(length=4, byteorder='big')
outFile = open(outFileName, 'w')

outFile.write(outBytes.hex())

outFile.close()
