import numpy as np
from PIL import Image

img = Image.open("IMG_2362.JPG")
out = img.convert("RGB")
img_array = np.array(out)

print(img_array.shape[0]*img_array.shape[1])
for x in range(0, img_array.shape[0]):
    if x%2==0:
        for y in range(0, img_array.shape[1]):
            if y%2==0:
                for z in range(1,img_array.shape[2]):
                    img_array[x][y][z]=0
            else:
                for z in range(0, img_array.shape[2], 2):
                    img_array[x][y][z] = 0
    else:
        for y in range(0, img_array.shape[1]):
            if y%2==0:
                for z in range(0, img_array.shape[2], 2):
                    img_array[x][y][z] = 0
            else:
                for z in range(0, img_array.shape[2] - 1):
                    img_array[x][y][z] = 0

#alcuni erano 3 zeri e perdevo dei bit
for x in range(0, img_array.shape[0]):
    for y in range(0, img_array.shape[1]):
        if img_array[x][y][0]==0 and img_array[x][y][1]==0 and img_array[x][y][2]==0:
            img_array[x][y][1]=1

img_array = img_array[img_array != 0]
img_array=np.array(img_array)
out=[]
for x in range(0,img_array.shape[0]):
    out.append((img_array[x]/0xFF) * 0x3FFF)

out=np.array(out).astype(np.float32)
OutputFile = open('OutputFilePath','wb')
OutputFile1= open('OutputFilePath1','wb')
BlockArray= np.array(out).astype(np.uint16)
Blockarray1= np.array(out).astype(np.uint8)
Blockarray1.tofile(OutputFile1)
BlockArray.tofile(OutputFile)
OutputFile.close()
OutputFile1.close()