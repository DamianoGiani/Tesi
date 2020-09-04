from PIL import Image
import numpy as np

img = Image.open("DanieleImgJPG")
out = img.convert("RGB")
img_array = np.array(out)

for x in range(0, img_array.shape[0],2):
    for y in range(0, img_array.shape[1],2):
        for z in range(1,img_array.shape[2]):
            img_array[x][y][z]=0

for x in range(0, img_array.shape[0],2):
    for y in range(1, img_array.shape[1],2):
        for z in range(0,img_array.shape[2],2):
            img_array[x][y][z]=0

for x in range(1, img_array.shape[0],2):
    for y in range(0, img_array.shape[1],2):
        for z in range(0,img_array.shape[2],2):
            img_array[x][y][z]=0

for x in range(1, img_array.shape[0],2):
    for y in range(1, img_array.shape[1],2):
        for z in range(0,img_array.shape[2]-1):
            img_array[x][y][z] = 0            #questi 4 for servono per mettere a 0 i colori filtrati dal CFA

img_array = img_array[img_array != 0]
lun = len(img_array)
my_list = []

for x in range(0,lun):
    b = img_array[x]
    bit_to_Double = b / 255
    c = int(round(bit_to_Double * 16383))
    my_list.append(c)
print(my_list) #converto ogni valore al relativo valore a 14 bit

my_list2 = []
l = len(my_list)

for x in range(0, l):
    b=bin(int(my_list[x]))[2:] #elimino i primi due bit che sono sempre uguali per la codifica di python
    c=b.zfill(14) #porto tutti gli elementi a 14 bit
    my_list2.append(c)
print(my_list2)

my_list3=[]
bin_str = "".join(my_list2)
print(bin_str)

def bitstring_to_bytes(s):  #stringhe di bit in byte
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

barray=[]

for index in range(int(len(bin_str)/8)):
    substring = bin_str[index * 8: index*8 + 8]
    barray.append(bitstring_to_bytes(substring))
bytearray=np.array(barray)

with open('image.bin', 'w') as f:
    for item in barray:
        f.write("%s" % item)  #crea file bin con i valori trasformati in byte

