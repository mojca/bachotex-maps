#!/usr/bin/env python

import numpy as np
import matplotlib
import matplotlib.image
# import matplotlib.image as mpimg
# from PIL import Image

filename_in  = "../png/bachotex-bw.png"
filename_out = "../png/bachotex-bw-corrected-layers.png"

im = matplotlib.image.imread(filename_in)
# img = Image.open(filname_in)

it = np.round(im[:,:,0]*10)
# it2 = it - 6*(it==10) + 1 + 64
# it3 = np.array(it2).transpose()

# lake: 62
# sand: 1->64
# paths: 3->64, 4->64
# grass: 2->65
# fence: 5->67
# house: 10->66
it2 = it + 62*(it==0) + 63*(it==1) + 61*(it==3) + 62*(it==4) + 63*(it==2) + 62*(it==5) + 56*(it==10)
it3 = np.array(it2).transpose()

matplotlib.image.imsave(filename_out, it3, vmin=0,vmax=128, cmap='gray')

# it = it.astype(np.uint8)
# matplotlib.image.imsave(filename_out, it, cmap='gray')

