#!/usr/bin/env python

import numpy as np
# import matplotlib
import matplotlib.image
from PIL import Image

filename_in  = "../png/bachotex-bw.png"
filename_out = "../png/bachotex-bw-corrected-layers.png"

im = matplotlib.image.imread(filename_in)
# im = Image.open(filename_in)

it = np.round(im[:,:,0]*10).astype(np.uint8)

it0 = np.zeros(np.shape(it))

num_lake =  0
num_sand =  1
num_gras =  2
num_path =  3
num_Path =  4
num_fenc =  5
num_hous = 10

col_lake =  -10
col_sand =   1
col_gras =   4
col_path =   5 # grass
col_Path =   2 # Path
col_fenc =   7
col_hous =   6 # house

it2 = it0 + \
    1*col_lake*(it==num_lake) + \
    1*col_sand*(it==num_sand) + \
    1*col_gras*(it==num_gras) + \
    1*col_path*(it==num_path) + \
    1*col_Path*(it==num_Path) + \
    1*col_fenc*(it==num_fenc) + \
    1*col_hous*(it==num_hous) + \
    128

j = Image.fromarray(it2.transpose().astype(np.uint8))
j.save(filename_out)

# for i in range(255):
#     t = np.sum(it2==i)
#     if t > 0:
#         print(i,t)
