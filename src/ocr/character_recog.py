#!/usr/bin/python2
from SimpleCV import Image

img = Image('good_test.jpg')
img = img.resize(img.width/2, img.height/2)
img = img.grayscale().edges().dilate(4).erode()
blobs = img.findBlobs()
img.show()
for b in blobs:
    b.show()
    raw_input()
    
