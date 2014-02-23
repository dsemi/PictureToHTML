#!/usr/bin/python2
import sys
from SimpleCV import Image
import subprocess
from shlex import split

def image_to_text(image):
    img = img.resize(img.width/2, img.height/2)
    img = img.grayscale().edges().dilate(4).erode()
    blobs = img.findBlobs()
    
    i = 0
    
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
