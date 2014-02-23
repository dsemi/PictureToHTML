#!/usr/bin/python2

def divs_from_boxes(box_list):
    return '<html><style> .outlined { border: 1px solid black;  } </style>\n%s\n</html>' % ('\n'.join(['<div class="outlined" style="position: absolute; left: %d; top: %d; width: %d; height: %d;">\n</div>' % box for box in box_list]))
    
def main():
    pass

if __name__ == '__main__':
    main()



