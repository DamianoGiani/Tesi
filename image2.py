from PIL import Image
import numpy as np

img = Image.open("file_example_TIFF_1MB.tiff")

img_array = np.array(img)

for x in range(0, img_array.shape[0], 2):
    for y in range(0, img_array.shape[1], 2):
        for z in range(1,img_array.shape[2]):
            img_array[x][y][z] = 0

for x in range(0, img_array.shape[0], 2):
    for y in range(1, img_array.shape[1], 2):
        for z in range(0,img_array.shape[2], 2):
            img_array[x][y][z] = 0

for x in range(0, img_array.shape[0], 2):
    for y in range(1, img_array.shape[1], 2):
        for z in range(0,img_array.shape[2], 3):
            img_array[x][y][z] = 0

for x in range(1, img_array.shape[0], 2):
    for y in range(0, img_array.shape[1], 2):
        for z in range(0,img_array.shape[2], 2):
            img_array[x][y][z] = 0

for x in range(1, img_array.shape[0], 2):
    for y in range(0, img_array.shape[1], 2):
        for z in range(0,img_array.shape[2],3):
            img_array[x][y][z]=0

for x in range(1, img_array.shape[0],2):
    for y in range(1, img_array.shape[1],2):
        for z in range(0,img_array.shape[2]-2):
            img_array[x][y][z]=0

for x in range(1, img_array.shape[0],2):
    for y in range(1, img_array.shape[1],2):
        for z in range(3,img_array.shape[2]):
            img_array[x][y][z]=0

print(img_array)
img1 = Image.fromarray(img_array, 'RGBA')
img1.show()

"""from PIL import Image
import numpy as np
xyz2rgb= (6602/10000,-841/10000,-939/10000,-4472/10000,12458/10000,2247/10000,-975/10000,2039/10000,6148/10000)
rgb2xyz = (
    0.412453, 0.357580, 0.180423,0,
    0.212671, 0.715160, 0.072169,0,
    0.019334, 0.119193, 0.950227,0)
im=Image.open("file_example_TIFF_1MB.tiff")
out=im.convert("RGB")
out1=out.convert("RGB",rgb2xyz)
out2=out1.convert("XYZ",xyz2rgb)"""""

