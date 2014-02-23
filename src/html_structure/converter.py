from SimpleCV import Image


def main():
    im_name = raw_input('Please enter image name')
    image = Image(im_name)

    # Find corners to boxes
    #image.grayscale().edges().show()
    image = image.grayscale().edges()
    image = image.smooth().dilate().erode()
    image = image.smooth().dilate().erode()

    blobs = image.binarize().findBlobs()

    # Gets all the boxes in the image
    boxes = [b.minRect() for b in blobs if b.area() > 200]

    # Draw all the boxes
    for b in boxes:
        (x,y) = map(min, zip(*b))
        (xmax,ymax) = map(max, zip(*b))
        
        width = xmax - x
        height = ymax - y
  
        print(str.format('Origin: ({0}, {1})\nWidth: {2}\nHeight: {3}\n', x, y, width, height))
        image.drawRectangle(x, y, width, height)
  
    image.show()
  
    raw_input()
  
if __name__ == '__main__':
    main()