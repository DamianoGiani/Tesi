
import numpy as np
from PIL import Image

img = Image.open("DanieleImgJPG")
out = img.convert("RGB")
img_array = np.array(out)
out_array = np.empty((img_array.shape[0], img_array.shape[1]))

print(img_array.shape[0 ] *img_array.shape[1])
for x in range(0, img_array.shape[0]):
    if x% 2 == 0:
        for y in range(0, img_array.shape[1]):
            if y % 2 == 0:
                out_array[x, y] = img_array[x, y, 0]
            else:
                out_array[x, y] = img_array[x, y, 1]
    else:
        for y in range(0, img_array.shape[1]):
            if y % 2 == 0:
                out_array[x, y] = img_array[x, y, 1]
            else:
                out_array[x, y] = img_array[x, y, 2]

out_array = (out_array.astype(np.float32) / 0xFF * 0x3FFF).astype(np.uint16)
with open('output_file.bin', 'wb') as stream:
    out_array.tofile(stream)