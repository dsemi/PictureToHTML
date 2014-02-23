#!/usr/bin/python2
import sys
from SimpleCV import Image
import subprocess
from shlex import split

def main():
    pass

def img_to_text(img):
    img = img.grayscale().edges().dilate(2).erode()
    img.show()
    raw_input()
    blobs = img.findBlobs()
    
    if blobs is None:
        return ''
        
    blobs = sorted(blobs, key=lambda blob: blob.x)
    
    text = ''
    
    for b in blobs:
        b = b.crop().invert()
        b.save(str.format('char.pgm'))
        p = subprocess.Popen(split('ocrad --charset=ascii char.pgm'), stdout=subprocess.PIPE)
        [output, errCode] = p.communicate()
        text += output.strip()
    
    return text
    
if __name__ == '__main__':
    main()
