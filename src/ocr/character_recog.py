#!/usr/bin/python2
from SimpleCV import Image

def main():
    im_name = raw_input('Please enter image name: ')
    img = Image(im_name)
    img = img.resize(img.width/2, img.height/2)
    img = img.grayscale().edges().dilate(4).erode()
    blobs = img.findBlobs()
    img.show()
    for b in blobs:
        b.show()
        raw_input()
    
if __name__ == '__main__':
    main()