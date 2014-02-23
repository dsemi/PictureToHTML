#!/usr/bin/python2

def divs_from_boxes(box_list):
    return '<html><style> .outlined { border: 1px solid black;  } </style>\n%s\n</html>' % ('\n'.join(['<div class="outlined" style="position: absolute; left: {x}; top: {y}; width: {width}; height: {height}; background:rgb({color[0]}, {color[1]}, {color[2]});">\n</div>'.format(**box) for box in box_list]))
    
def main():
    pass

if __name__ == '__main__':
    main()


