from SimpleCV import Image
from HTMLGenerator import divs_from_boxes
from character_recog import img_to_text

def main():
    out = convert("test.jpg")
    with open("output.html", 'w') as f:
        f.write(out)

def convert(img):
    image = Image(img)
    boxes = extract_div_info(image)
    return divs_from_boxes(boxes)
      

def extract_div_info(image):
    RECT_TOL = 0.1     # How close to rectangle?
    MIN_AREA = 500      # Min number of pixels in an element
    NEAREST_EDGE = 20   # Num pixels from another edge
    MAX_HEIGHT = 700.0  # Page height
    BUTTON_TOL = 10      # Num pixels from corner
    
    # Resize Image
    f = MAX_HEIGHT / image.height
    image = r_image = image.resize(int(image.width * f), int(image.height * f))

    # Find corners to boxes
    image = image.grayscale().edges()
    image = image.smooth().dilate().erode()
    image = image.smooth().dilate().erode()
    image = image.binarize()

    blobs = image.findBlobs()

    # Gets all the rectangles in the image
    rects = [b.minRect() for b in blobs if 
             b.isRectangle(RECT_TOL) 
             and b.area() > MIN_AREA 
             and b.distanceToNearestEdge() > NEAREST_EDGE]
    
    
    # Formats all box data for HTML gen
    boxes = []
    for r in rects:
        (x,y) = map(min, zip(*r))
        (xmax,ymax) = map(max, zip(*r))
        w = xmax - x
        h = ymax - y
        
        i = (r_image*2).crop(x, y, w, h)
        c = map(int, i.meanColor())
        d = -i.area()
        
        # Determines element type
        cropped = image.crop(x, y, w, h)
        c_blobs = cropped.findBlobs()
        
        # Gets the text
        text = img_to_text(r_image.crop(x, y, w, h))

        # Determines if this is a button
        tag = 'div'
        for c_blob in c_blobs :
            c_r = c_blob.minRect()
            (c_x,c_y) = map(min, zip(*c_r))
            (c_xmax, c_ymax) = map(max, zip(*c_r))
            c_w = c_xmax - c_x
            c_h = c_ymax - c_y
            
            if c_blob.area() < MIN_AREA and c_blob.isSquare(1, 0.5) and abs(c_xmax-w) < BUTTON_TOL and c_y < BUTTON_TOL :
                tag = 'button'
        
        iw = image.width
        ih = image.height
        boxes.append({'tag':tag, 
                      'x' : x / iw * 100, 
                      'y' : y / ih * 100, 
                      'width' : w / iw * 100, 
                      'height': h / ih * 100,
                      'color':c, 'depth':d, 'text':text})
  
	#image.drawRectangle(x, y, width, height)
  
    #image.show()
    
    return boxes
  
if __name__ == '__main__':
    main()
