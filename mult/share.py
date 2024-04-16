#input a number as input to the computation and two output share file names
#output two files with shares of the number

import sys
import os
import math

#biggest prime that fits in 31 bits
#useful resource: https://t5k.org/lists/2small/
P = 2**31-1

#check for right number of params
if len(sys.argv) != 4:
    print("wrong number of params!")
    sys.exit()

input = int(sys.argv[1])
s1FileName = str(sys.argv[2])
s2FileName = str(sys.argv[3])

#generate cryptographic random bytes to use in producing shares
#no other randomness should be used beyond this
randBytes = os.urandom(math.ceil(math.log2(P)))

#TODO produce shares s1 and s2
#hint: you need to convert randBytes to an integer mod P
rand_int = int.from_bytes(randBytes, byteorder='big')
s1 = (rand_int) % P
s2 = (input - rand_int) % P

s1Bytes = s1.to_bytes(length=4, byteorder='big')
s2Bytes = s2.to_bytes(length=4, byteorder='big')

#write the shares to the given files
s1File = open(s1FileName, "w")
s2File = open(s2FileName, "w")
s1File.write(s1Bytes.hex())
s2File.write(s2Bytes.hex())
s1File.close()
s2File.close()
