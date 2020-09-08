import numpy as np
from PIL import Image

img = (np.fromfile('temp.out', dtype=np.uint16).astype(np.float32) / 0x3FFF * 0xFF).astype(np.uint8).reshape((3529, 5280))
print(img)
i=Image.fromarray(img)
i.save('gray.png')
img = Image.open("gray.png")
out = img.convert("RGB")
img_array=np.array(out)

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
            img_array[x][y][z] = 0

img1 = Image.fromarray(img_array, 'RGB')
img1.show()
img1.save('RGB.png')