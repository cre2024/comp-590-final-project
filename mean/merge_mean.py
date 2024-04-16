#input two filenames with shares to be merged and the number of data points
#output the sum and the mean

import sys
import os

P = 2**31-1

#check for right number of params
if len(sys.argv) != 4:
    print("wrong number of params!")
    sys.exit()

s1FileName = str(sys.argv[1])
s2FileName = str(sys.argv[2])
numInputs = int(sys.argv[3])

s1File = open(s1FileName, "r")
s2File = open(s2FileName, "r")

s1Bytes = bytes.fromhex(s1File.read())
s2Bytes = bytes.fromhex(s2File.read())

s1Output = int.from_bytes(s1Bytes, byteorder='big')
s2Output = int.from_bytes(s2Bytes, byteorder='big')

s1File.close()
s2File.close()

sum = (s1Output + s2Output) % P
mean = sum / numInputs

print("sum: " + str(sum))
print("mean: " + str(mean))

