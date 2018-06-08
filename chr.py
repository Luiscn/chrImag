import os
import numpy as np

from ultil import *

from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import rescale, downscale_local_mean

path = './input/'
imsize = 128

img_id = listdir_nohidden(path)
img = imread(img_id[0])
data = rgb2gray(img)
data = rescale(data, imsize/np.shape(data)[1])
data = downscale_local_mean(data, (2, 1))
data, s = imtrans(data)
write_file(data, s)