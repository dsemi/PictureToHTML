import sys
from SimpleCV import Image


def main():
    RECT_TOL = 0.5
    MIN_AREA = 500
    NEAREST_EDGE = 20
    MAX_HEIGHT = 700.0
    
  
    image = Image(sys.argv[1])
    
    # Resize Image
    f = MAX_HEIGHT / image.height
    image = image.resize(int(image.width * f), int(image.height * f))

    # Find corners to boxes
    image = image.grayscale().edges()
    image = image.smooth().dilate().erode()
    image = image.smooth().dilate().erode()
    image = image.binarize()

    blobs = image.findBlobs()

    # Gets all the boxes in the image
    boxes = [b.minRect() for b in blobs if 
	     b.isRectangle(RECT_TOL) 
	     and b.area() > MIN_AREA 
	     and b.distanceToNearestEdge() > NEAREST_EDGE]

    # Draw all the boxes
    for b in boxes:
        (x,y) = map(min, zip(*b))
        (xmax,ymax) = map(magitx, zip(*b))
        
        width = xmax - x
        height = ymax - y
  
	image.drawRectangle(x, y, width, height)
  
    image.show()
  
if __name__ == '__main__':
    main()