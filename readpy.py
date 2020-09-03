
import numpy as np
array=[]

with open("temp.bin", "rb") as f:
    byte = f.read(1)
    while byte:
        array.append(byte)
        byte = f.read(1)
#print(array)
list=[]
for x in range(0, 14):
    k = np.frombuffer(array[x], dtype=np.uint8)
    list.append(np.unpackbits(k).reshape(8))
list = np.array(list)
l=len(list)
my_list=(np.reshape(list,l*8))
pixel=[]

for x in range(0,int(len(my_list)/14)):
    pixel.append(my_list[x* 14: x*14 + 14])

pixel=np.array(pixel)
print(pixel[0])
rgbarray=[]
for x in range(0,len(pixel)):
    i = (pixel[x].dot(2 ** np.arange(14)[::-1]))
    rgbarray.append(int(round((i/16383)*255)))
rgbarray=np.array(rgbarray)
print(rgbarray)
"""
i=(pixel[0].dot(2**np.arange(14)[::-1]))
print(i)
i=int(round((i/16383)*255))
print(i)
"""
#list=list.tolist()

"""
'''
def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] & (1<<shift)) >> shift

x=[access_bit(array,i) for i in range(len(array)*8)]
print(x)'''
#x=[access_bit(array,i) for i in range(len(array)*8)]

#firstfivebits = byte >> 2
"""
"""
while byte:
    print(byte)
    byte = file.read(1)
file.close()"""