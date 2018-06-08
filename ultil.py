import os
import glob
import numpy as np

def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))

def imlinmap(im, limIn, limOut):
    ratio=(limOut[1]-limOut[0])/(limIn[1]-limIn[0])
    im=im-limIn[0]
    im=im*ratio
    im=im+limOut[0]
    return im


def imtrans(im):
    im = imlinmap(im, [np.max(im), np.min(im)], [0, 15]).astype('uint8')
    s = np.shape(im)
    im = np.reshape(im, (1, -1))
    im = np.squeeze(im)
    return im, s

def write_file(data, sh):
    file_name = 'log.txt'
    dim = sh[1] * sh[0]
    with open(file_name, 'wb') as x_file:
        for n in range(dim):
            x_file.write(chrCase(data[n]).encode())
            if ((n+1) % sh[1] == 0):
                x_file.write('\n'.encode())

def chrCase(x):
    return {
        0: ' ',
        1: '.',
        2: '-',
        3: '^',
        4: '+',
        5: '=',
        6: '*',
        7: '7',
        8: '3',
        9: 'U',
        10:'0',
        11:'8',
        12:'K',
        13:'#',
        14:'M',
        15:'@',
    }[x]