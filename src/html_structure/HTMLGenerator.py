#!/usr/bin/python2

PAGE_TEMPLATE = '''
<html>
<style>
.outlined {
border: 1px solid black;
}
</style>
%s
</html>'''

DIV_TEMPLATE = '''
<div class="outlined" style="position: absolute;
left: {x}; top: {y}; width: {width}; height: {height};
background:rgb({color[2]}, {color[1]}, {color[0]}); z-index:{depth}">
</div>'''


# As of right now this is very barebones, when more features of html are added, make class and have generators for different objects
# Then also move outer html out to another function

def divs_from_boxes(box_list):
    return PAGE_TEMPLATE % ('\n'.join([DIV_TEMPLATE.format(**box) for box in box_list]))
    
def main():
    pass

if __name__ == '__main__':
    main()



