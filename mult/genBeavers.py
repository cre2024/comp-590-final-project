#no inputs
#output shares a_1,b_1,c_1 and a_2,b_2,c_2 in two .txt files

import sys
import os
import math

#biggest prime that fits in 31 bits
#useful resource: https://t5k.org/lists/2small/
P = 2**31-1

a1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P
a2 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P

b1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P
b2 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P

c1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P

a = (a1 + a2) % P
b = (b1 + b2) % P
c = a * b % P

c1 = int.from_bytes(os.urandom(math.ceil(math.log2(P))), byteorder='big') % P
c2 = c - c1
if c2 < 0:
	c2 = P + c2

a1Bytes = a1.to_bytes(length=4, byteorder='big')
a2Bytes = a2.to_bytes(length=4, byteorder='big')
b1Bytes = b1.to_bytes(length=4, byteorder='big')
b2Bytes = b2.to_bytes(length=4, byteorder='big')
c1Bytes = c1.to_bytes(length=4, byteorder='big')
c2Bytes = c2.to_bytes(length=4, byteorder='big')

s1File = open("abc_1.txt", 'w')
s2File = open("abc_2.txt", 'w')

s1File.writelines([a1Bytes.hex()+"\n", b1Bytes.hex()+"\n", c1Bytes.hex()+"\n"])
s2File.writelines([a2Bytes.hex()+"\n", b2Bytes.hex()+"\n", c2Bytes.hex()+"\n"])

s1File.close()
s2File.close()
