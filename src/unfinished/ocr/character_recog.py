#!/usr/bin/python2
import sys
from SimpleCV import Image

def main():
    img = Image(sys.argv[1])
    img = img.resize(img.width/2, img.height/2)
    img = img.grayscale().edges().dilate(4).erode()
    blobs = img.findBlobs()
    img.show()
    for b in blobs:
        b = b.crop()
        b.show()
        raw_input()
    
if __name__ == '__main__':
    main()