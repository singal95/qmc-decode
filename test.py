from ctypes import *

dlib = cdll.LoadLibrary('./build/libqmc_decode.dylib')
src = 'jap.mp3'
dest = 'jap.mp3.ep'
for i in range(10):
    if i >= 1:
        if i % 2 == 0:
            src = dest
            dest = '.'.join([src, 'ep'])
        else:
            src = dest
            dest = '.'.join([src, 'mp3'])
    print(src, dest)

    dlib.encode_decode(bytes(src, encoding='ascii'), bytes(dest, encoding='ascii'))


