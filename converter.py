from SimpleCV import Image, Color

image = Image('test.jpg')

# Find corners to boxes
#image.grayscale().edges().show()
image = image.grayscale().edges()
image = image.smooth().dilate().erode()
image = image.smooth().dilate().erode()

blobs = image.binarize().findBlobs()

# Gets all the boxes in the image
boxes = []
for b in blobs :
  if b.area() > 200:
    boxes.append(b.minRect())

# Draw all the boxes
for b in boxes :
  x = min(b[0][0], b[1][0], b[2][0], b[3][0])
  y = min(b[0][1], b[1][1], b[2][1], b[3][1])
  
  xmax = max(b[0][0], b[1][0], b[2][0], b[3][0])
  ymax = max(b[0][1], b[1][1], b[2][1], b[3][1])
  
  width = xmax - x
  height = ymax - y
  
  print str.format('Origin: ({0}, {1})\nWidth: {2}\nHeight: {3}\n', x, y, width, height);
  image.drawRectangle(x, y, width, height)
  
image.show()

  
raw_input()
  
# fitContour()