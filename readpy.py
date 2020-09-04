from PIL import Image
import numpy as np
array = []

with open("temp.bin", "rb") as f:
    byte = f.read(1)
    while byte:
        array.append(byte)
        byte = f.read(1)

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

pixel=np.array(pixel)  #ho creato un array dove ogni elemento sono i 14 bit estratti dal file .bin

rgbarray=[]
for x in range(0,len(pixel)):
    i = (pixel[x].dot(2 ** np.arange(14)[::-1]))
    rgbarray.append(int(round((i/16383)*255)))  #ho creato un array dove ogni elemento rappresenta i 14 bit convertiti in valore RGB
rgbarray=np.array(rgbarray)

#5280*3529
distance = [[[0 for k in range(3)] for j in range(5280)] for i in range(3529)] #creo array di 0

distance=np.array(distance)
B = np.reshape(rgbarray, (-1, 5280))
print(B)
arrayred=[]
arraygreen=[]
arrayblue=[]
for index in range(0,B.shape[0],2):
    for x in range(0,B.shape[1],2):
        arrayred.append(B[index][x])
arrayred=np.array(arrayred)     #creo array con tutti i valori del Rosso

for index in range(0,B.shape[0],2):
    for x in range(1,B.shape[1],2):
        arraygreen.append(B[index][x])
    for x in range(1, B.shape[1], 2):
        if (index+1)!=3529:
            arraygreen.append(B[index+1][x-1]) #creo array con tutti i valori del Verdi

arraygreen=np.array(arraygreen)

for index in range(1,B.shape[0],2):
    for x in range(1,B.shape[1],2):
        arrayblue.append(B[index][x])   #creo array con tutti i valori del Blu

arrayblue=np.array(arrayblue)

i=0
for x in range(0, distance.shape[0],2):         #questi 3 cicli annidati aggiungono i valori dagli array alle relative posizioni rgb
    for y in range(0, distance.shape[1],2):
        for z in range(0,distance.shape[2],3):
            distance[x][y][z]=arrayred[i]
            i=i+1

j=0
for x in range(0, distance.shape[0],1):
    if x%2==0:
        for y in range(1, distance.shape[1],2):
            for z in range(1,distance.shape[2],2):
                distance[x][y][z]=arraygreen[j]
                j=j+1
    else:
        for y in range(0, distance.shape[1],2):
            for z in range(1,distance.shape[2],2):
                distance[x][y][z]=arraygreen[j]
                j=j+1

k=0
for x in range(1, distance.shape[0],2):
    for y in range(1, distance.shape[1],2):
        for z in range(2,distance.shape[2]):
            distance[x][y][z]=arrayblue[k]
            k=k+1



print(distance)

img4 = Image.fromarray(distance, 'RGB')         #viene fuori tutta un'altra cosa
img4.show()

