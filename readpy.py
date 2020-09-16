'''from PIL import Image
import numpy as np
img = (np.fromfile('tempmio.out', dtype=np.uint16).astype(np.float32) / 0x3FFF * 0xFF).astype(np.uint8).reshape((-1,5280))#3456  #5280
print(img)
img=Image.fromarray(img)
img.save('gray.png')

#img.save('gray.png')
#!/usr/bin/env python3
'''
import argparse

import colour_demosaicing
import numpy as np
from PIL import Image




data = (np.fromfile('tempmio.out', dtype=np.dtype('u2')).reshape((3456,-1)).astype(np.float64) / 0x3FFF)
data = colour_demosaicing.demosaicing_CFA_Bayer_bilinear(data)
data = (data * 0xFF).astype(np.uint8)
img = Image.fromarray(data)
img.show()