
import numpy as np
array=[]

with open("temp.bin", "rb") as f:
    byte = f.read(1)
    while byte:
        array.append(byte)
        byte = f.read(1)
#print(array)
list=[]
for x in range(0, len(array)):
    k = np.frombuffer(array[x], dtype=np.uint8)
    list.append(np.unpackbits(k).reshape(8))
list = np.array(list)
l=len(list)
my_list=(np.reshape(list,l*8))
pixel=[]

for x in range(0,int(len(my_list)/14)):
    pixel.append(my_list[x* 14: x*14 + 14])

pixel=np.array(pixel)

rgbarray=[]
for x in range(0,len(pixel)):
    i = (pixel[x].dot(2 ** np.arange(14)[::-1]))
    rgbarray.append(int(round((i/16383)*255)))
rgbarray=np.array(rgbarray)
print(rgbarray)

with open('rgb.txt','w') as f:
    for item in rgbarray:
        f.write("%s "% item)
my_rgb=[[[]]]
